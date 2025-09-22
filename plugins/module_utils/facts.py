#
# Copyright (c) 2018 Cisco and/or its affiliates.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class FmcFactsBase(object):
    """Base class for FMC facts gathering"""

    def __init__(self, resource):
        self.resource = resource

    def gather_facts(self, gather_subset, domain_uuid=None):
        """Main facts gathering method"""
        # Normalize gather_subset for performance optimization
        if 'all' in gather_subset:
            gather_subset = ['domains', 'devices', 'access_policies', 'file_policies',
                             'intrusion_policies', 'physical_interfaces', 'network_objects',
                             'port_objects', 'security_zones', 'device_groups']
        elif 'min' in gather_subset:
            # Essential facts only - much faster for large FMCs
            gather_subset = ['domains', 'devices', 'access_policies', 'file_policies', 'intrusion_policies']

        facts = {'fmc': {}}

        # Always gather domains first if requested or if we need domain info for other operations
        domains = []
        if 'domains' in gather_subset or domain_uuid is None:
            domains = self._gather_domains()
            if not isinstance(domains, list):
                raise ValueError(f"Expected domains to be a list, got {type(domains)}: {domains}")

            # Debug each domain structure
            for i, domain in enumerate(domains):
                if not isinstance(domain, dict):
                    raise ValueError(f"Domain {i} is not a dict. Type: {type(domain)}, Value: {domain}")
                if 'uuid' not in domain and 'id' not in domain:
                    raise ValueError(f"Domain {i} missing uuid/id. Keys: {list(domain.keys()) if isinstance(domain, dict) else 'Not a dict'}")

            facts['fmc']['domains'] = domains

        # Determine which domains to process
        target_domains = []
        if domain_uuid:
            # Use specific domain if provided
            target_domains = [{'uuid': domain_uuid}]
        elif domains:
            # Use all discovered domains
            target_domains = domains

        # Debug target domains
        for i, domain in enumerate(target_domains):
            if not isinstance(domain, dict):
                raise ValueError(f"target_domains[{i}] is not a dict. Type: {type(domain)}, Value: {domain}")

        # Gather facts for each domain
        if target_domains:
            for subset in gather_subset:
                if subset == 'domains':
                    continue  # Already handled above

                # Initialize the subset dictionary
                if subset not in facts['fmc']:
                    facts['fmc'][subset] = {}

                for domain in target_domains:
                    # Extremely defensive domain handling
                    domain_id = None

                    try:
                        if isinstance(domain, dict):
                            domain_id = domain.get('uuid') or domain.get('id')
                        elif isinstance(domain, str):
                            # If domain is just a string UUID, use it directly
                            domain_id = domain
                        else:
                            raise ValueError(f"Unexpected domain type: {type(domain)}")

                        if not domain_id:
                            raise ValueError(f"No domain_id found in domain: {domain}")

                    except Exception as e:
                        raise ValueError(f"Error processing domain {domain}: {e}")

                    if subset == 'devices':
                        facts['fmc'][subset][domain_id] = self._gather_devices(domain_id)
                    elif subset == 'access_policies':
                        facts['fmc'][subset][domain_id] = self._gather_access_policies(domain_id)
                    elif subset == 'file_policies':
                        facts['fmc'][subset][domain_id] = self._gather_file_policies(domain_id)
                    elif subset == 'intrusion_policies':
                        facts['fmc'][subset][domain_id] = self._gather_intrusion_policies(domain_id)
                    elif subset == 'physical_interfaces':
                        # Only gather if devices are available
                        if 'devices' in facts['fmc'] and domain_id in facts['fmc']['devices']:
                            interface_data = {}
                            for device in facts['fmc']['devices'][domain_id]:
                                device_id = device.get('id')
                                if device_id:
                                    interface_data[device_id] = self._gather_physical_interfaces(domain_id, device_id)
                            facts['fmc'][subset][domain_id] = interface_data
                        else:
                            facts['fmc'][subset][domain_id] = {}
                    elif subset == 'network_objects':
                        facts['fmc'][subset][domain_id] = self._gather_network_objects(domain_id)
                    elif subset == 'port_objects':
                        facts['fmc'][subset][domain_id] = self._gather_port_objects(domain_id)
                    elif subset == 'security_zones':
                        facts['fmc'][subset][domain_id] = self._gather_security_zones(domain_id)
                    elif subset == 'device_groups':
                        facts['fmc'][subset][domain_id] = self._gather_device_groups(domain_id)

        return facts

    def _gather_domains(self):
        """Gather domain facts"""
        try:
            params = {}
            result = self.resource.execute_operation('getAllDomain', params)
            # Ensure we return a list of dictionaries
            if isinstance(result, list):
                return result
            elif isinstance(result, dict) and 'items' in result:
                return result['items']
            else:
                # Return empty list if unexpected format
                return []
        except Exception as e:
            # Return empty list if operation fails
            return []

    def _gather_devices(self, domain_uuid):
        """Gather device facts for a specific domain"""
        try:
            params = {'path_params': {'domainUUID': domain_uuid}}
            result = self.resource.execute_operation('getAllDevice', params)
            # Handle different response formats
            if isinstance(result, list):
                return result
            elif isinstance(result, dict) and 'items' in result:
                return result['items']
            else:
                return []
        except Exception as e:
            # Return empty list if operation fails
            return []

    def _gather_access_policies(self, domain_uuid):
        """Gather access policy facts for a specific domain"""
        try:
            params = {'path_params': {'domainUUID': domain_uuid}}
            result = self.resource.execute_operation('getAllAccessPolicy', params)
            # Handle different response formats
            if isinstance(result, list):
                return result
            elif isinstance(result, dict) and 'items' in result:
                return result['items']
            else:
                return []
        except Exception as e:
            # Return empty list if operation fails
            return []

    def _gather_file_policies(self, domain_uuid):
        """Gather file policy facts for a specific domain"""
        try:
            params = {'path_params': {'domainUUID': domain_uuid}}
            result = self.resource.execute_operation('getAllFilePolicy', params)
            # Handle different response formats
            if isinstance(result, list):
                return result
            elif isinstance(result, dict) and 'items' in result:
                return result['items']
            else:
                return []
        except Exception as e:
            # Return empty list if operation fails
            return []

    def _gather_intrusion_policies(self, domain_uuid):
        """Gather intrusion policy facts for a specific domain"""
        try:
            params = {'path_params': {'domainUUID': domain_uuid}}
            result = self.resource.execute_operation('getAllIntrusionPolicy', params)
            # Handle different response formats
            if isinstance(result, list):
                return result
            elif isinstance(result, dict) and 'items' in result:
                return result['items']
            else:
                return []
        except Exception as e:
            # Return empty list if operation fails
            return []

    def _gather_physical_interfaces(self, domain_uuid, device_id):
        """Gather physical interface facts for a specific device"""
        try:
            params = {
                'path_params': {
                    'domainUUID': domain_uuid,
                    'containerUUID': device_id
                }
            }
            result = self.resource.execute_operation('getAllFTDPhysicalInterface', params)
            # Handle different response formats
            if isinstance(result, list):
                return result
            elif isinstance(result, dict) and 'items' in result:
                return result['items']
            else:
                return []
        except Exception as e:
            # Return empty list if operation fails
            return []

    def _gather_network_objects(self, domain_uuid):
        """Gather network object facts for a specific domain"""
        try:
            params = {'path_params': {'domainUUID': domain_uuid}}
            result = self.resource.execute_operation('getAllNetworkObject', params)
            # Handle different response formats
            if isinstance(result, list):
                return result
            elif isinstance(result, dict) and 'items' in result:
                return result['items']
            else:
                return []
        except Exception as e:
            # Return empty list if operation fails
            return []

    def _gather_port_objects(self, domain_uuid):
        """Gather port object facts for a specific domain"""
        try:
            params = {'path_params': {'domainUUID': domain_uuid}}
            result = self.resource.execute_operation('getAllPortObject', params)
            # Handle different response formats
            if isinstance(result, list):
                return result
            elif isinstance(result, dict) and 'items' in result:
                return result['items']
            else:
                return []
        except Exception as e:
            # Return empty list if operation fails
            return []

    def _gather_security_zones(self, domain_uuid):
        """Gather security zone facts for a specific domain"""
        try:
            params = {'path_params': {'domainUUID': domain_uuid}}
            result = self.resource.execute_operation('getAllSecurityZoneObject', params)
            # Handle different response formats
            if isinstance(result, list):
                return result
            elif isinstance(result, dict) and 'items' in result:
                return result['items']
            else:
                return []
        except Exception as e:
            # Return empty list if operation fails
            return []

    def _gather_device_groups(self, domain_uuid):
        """Gather device group facts for a specific domain"""
        try:
            params = {'path_params': {'domainUUID': domain_uuid}}
            result = self.resource.execute_operation('getAllDeviceGroupObject', params)
            # Handle different response formats
            if isinstance(result, list):
                return result
            elif isinstance(result, dict) and 'items' in result:
                return result['items']
            else:
                return []
        except Exception as e:
            # Return empty list if operation fails
            return []
