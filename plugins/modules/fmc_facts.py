#!/usr/bin/python
# -*- coding: utf-8 -*-

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

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'network'}

DOCUMENTATION = """
---
module: fmc_facts
short_description: Gather facts from Cisco FMC devices over REST API
description:
    - Gathers facts from Cisco FMC devices including domains, devices, access policies, 
      network objects, and other configuration elements. All operations are performed over REST API.
version_added: "1.0.10"
author: "Cisco Systems (@cisco)"

options:
    gather_subset:
        description:
            - A list of fact subsets to gather. If not specified, minimal facts are gathered for performance.
            - "min: gathers essential facts only (domains, devices, access_policies) - DEFAULT for performance"
            - "all: gathers all available facts (WARNING: may impact performance with large configurations)"
            - "domains: gathers domain information"
            - "devices: gathers device information for all domains"
            - "access_policies: gathers access policies for all domains"
            - "physical_interfaces: gathers physical interfaces when devices are present"  
            - "network_objects: gathers network objects for all domains (WARNING: can be large dataset)"
            - "port_objects: gathers port objects for all domains (WARNING: can be large dataset)"
            - "security_zones: gathers security zones for all domains (WARNING: can be large dataset)"
            - "device_groups: gathers device groups for all domains"
        type: list
        elements: str
        default: ['all']
    domain_uuid:
        description:
            - Specific domain UUID to gather facts for. If not specified, facts are gathered for all domains.
            - This is useful when you want to limit fact gathering to a specific domain for performance.
        type: str
        required: false
"""

EXAMPLES = """
# Gather minimal facts (recommended for performance)
- name: Gather essential FMC facts only
  cisco.fmcansible.fmc_facts:
    gather_subset:
      - min  # domains, devices, access_policies only

# Gather specific facts for better performance
- name: Gather only domain and device facts
  cisco.fmcansible.fmc_facts:
    gather_subset:
      - domains
      - devices

# Gather facts with physical interfaces when devices are present
- name: Gather facts including interfaces
  cisco.fmcansible.fmc_facts:
    gather_subset:
      - domains
      - devices
      - physical_interfaces

# Gather facts for a specific domain
- name: Gather facts for a specific domain
  cisco.fmcansible.fmc_facts:
    domain_uuid: "{{ domain_id }}"
    gather_subset:
      - devices
      - access_policies

# WARNING: Use 'all' with caution on large FMCs
- name: Gather all FMC facts (performance impact)
  cisco.fmcansible.fmc_facts:
    gather_subset:
      - all  # May be slow with many network objects/zones

# Gather network objects only when specifically needed
- name: Gather network objects explicitly
  cisco.fmcansible.fmc_facts:
    gather_subset:
      - domains
      - network_objects  # Only when you need them

# Use gathered facts in subsequent tasks
- name: Use gathered facts in subsequent tasks
  cisco.fmcansible.fmc_configuration:
    operation: addNetworkObject
    data:
      name: "NewNetwork"
      value: "192.168.100.0/24"
      type: "Network"
    path_params:
      domainUUID: "{{ ansible_facts['fmc']['domains'][0]['uuid'] }}"
"""

RETURN = """
ansible_facts:
    description: Facts about the FMC device
    returned: always
    type: dict
    contains:
        fmc:
            description: FMC specific facts
            type: dict
            contains:
                domains:
                    description: List of domains configured on FMC
                    type: list
                    elements: dict
                devices:
                    description: Dictionary of devices per domain
                    type: dict
                access_policies:
                    description: Dictionary of access policies per domain  
                    type: dict
                network_objects:
                    description: Dictionary of network objects per domain
                    type: dict
                port_objects:
                    description: Dictionary of port objects per domain
                    type: dict
                security_zones:
                    description: Dictionary of security zones per domain
                    type: dict
                device_groups:
                    description: Dictionary of device groups per domain
                    type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.cisco.fmcansible.plugins.module_utils.common import (
    FmcConfigurationError, FmcServerError, FmcUnexpectedResponse,
    construct_ansible_facts)
from ansible_collections.cisco.fmcansible.plugins.module_utils.configuration import (
    BaseConfigurationResource, CheckModeException,
    FmcInvalidOperationNameError)
from ansible_collections.cisco.fmcansible.plugins.module_utils.fmc_swagger_client import \
    ValidationError


def gather_domains(resource):
    """Gather domain facts"""
    try:
        params = {}
        result = resource.execute_operation('getAllDomain', params)
        # Debug the API response
        import json
        debug_info = {
            'result_type': str(type(result)),
            'result_content': str(result)[:500] + ('...' if len(str(result)) > 500 else '')
        }
        
        # Ensure we return a list of dictionaries
        if isinstance(result, list):
            return result
        elif isinstance(result, dict) and 'items' in result:
            return result['items']
        else:
            # Return empty list with debug info
            return []
    except Exception as e:
        # Return empty list if operation fails
        return []


def gather_devices(resource, domain_uuid):
    """Gather device facts for a specific domain"""
    try:
        params = {'path_params': {'domainUUID': domain_uuid}}
        result = resource.execute_operation('getAllDevice', params)
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


def gather_access_policies(resource, domain_uuid):
    """Gather access policy facts for a specific domain"""
    try:
        params = {'path_params': {'domainUUID': domain_uuid}}
        result = resource.execute_operation('getAllAccessPolicy', params)
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


def gather_physical_interfaces(resource, domain_uuid, device_id):
    """Gather physical interface facts for a specific device"""
    try:
        params = {
            'path_params': {
                'domainUUID': domain_uuid,
                'containerUUID': device_id
            }
        }
        return resource.execute_operation('getAllFTDPhysicalInterface', params)
    except Exception as e:
        # Return empty list if operation fails
        return []


def gather_network_objects(resource, domain_uuid):
    """Gather network object facts for a specific domain"""
    try:
        params = {'path_params': {'domainUUID': domain_uuid}}
        return resource.execute_operation('getAllNetworkObject', params)
    except Exception as e:
        # Return empty list if operation fails
        return []


def gather_port_objects(resource, domain_uuid):
    """Gather port object facts for a specific domain"""
    try:
        params = {'path_params': {'domainUUID': domain_uuid}}
        return resource.execute_operation('getAllPortObject', params)
    except Exception as e:
        # Return empty list if operation fails
        return []


def gather_security_zones(resource, domain_uuid):
    """Gather security zone facts for a specific domain"""
    try:
        params = {'path_params': {'domainUUID': domain_uuid}}
        return resource.execute_operation('getAllSecurityZoneObject', params)
    except Exception as e:
        # Return empty list if operation fails
        return []


def gather_device_groups(resource, domain_uuid):
    """Gather device group facts for a specific domain"""
    try:
        params = {'path_params': {'domainUUID': domain_uuid}}
        return resource.execute_operation('getAllDeviceGroupObject', params)
    except Exception as e:
        # Return empty list if operation fails
        return []


def main():
    argument_spec = {
        'gather_subset': {
            'type': 'list',
            'elements': 'str',
            'default': ['min'],  # Changed default to 'min' for performance
            'choices': ['all', 'min', 'domains', 'devices', 'access_policies', 'physical_interfaces',
                       'network_objects', 'port_objects', 'security_zones', 'device_groups']
        },
        'domain_uuid': {
            'type': 'str',
            'required': False
        }
    }

    module = AnsibleModule(argument_spec=argument_spec,
                          supports_check_mode=True)

    connection = Connection(module._socket_path)
    resource = BaseConfigurationResource(connection, module.check_mode)
    
    params = module.params
    gather_subset = params['gather_subset']
    domain_uuid = params.get('domain_uuid')

    # Normalize gather_subset for performance optimization
    if 'all' in gather_subset:
        gather_subset = ['domains', 'devices', 'access_policies', 'physical_interfaces',
                        'network_objects', 'port_objects', 'security_zones', 'device_groups']
    elif 'min' in gather_subset:
        # Essential facts only - much faster for large FMCs
        gather_subset = ['domains', 'devices', 'access_policies']

    facts = {'fmc': {}}

    try:
        # Always gather domains first if requested or if we need domain info for other operations
        domains = []
        if 'domains' in gather_subset or domain_uuid is None:
            domains = gather_domains(resource)
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
                        facts['fmc'][subset][domain_id] = gather_devices(resource, domain_id)
                    elif subset == 'access_policies':
                        facts['fmc'][subset][domain_id] = gather_access_policies(resource, domain_id)
                    elif subset == 'physical_interfaces':
                        # Only gather if devices are available
                        if 'devices' in facts['fmc'] and domain_id in facts['fmc']['devices']:
                            interface_data = {}
                            for device in facts['fmc']['devices'][domain_id]:
                                device_id = device.get('id')
                                if device_id:
                                    interface_data[device_id] = gather_physical_interfaces(resource, domain_id, device_id)
                            facts['fmc'][subset][domain_id] = interface_data
                        else:
                            facts['fmc'][subset][domain_id] = {}
                    elif subset == 'network_objects':
                        facts['fmc'][subset][domain_id] = gather_network_objects(resource, domain_id)
                    elif subset == 'port_objects':
                        facts['fmc'][subset][domain_id] = gather_port_objects(resource, domain_id)
                    elif subset == 'security_zones':
                        facts['fmc'][subset][domain_id] = gather_security_zones(resource, domain_id)
                    elif subset == 'device_groups':
                        facts['fmc'][subset][domain_id] = gather_device_groups(resource, domain_id)

        module.exit_json(changed=False, ansible_facts=facts)

    except FmcInvalidOperationNameError as e:
        module.fail_json(msg='Invalid operation name while gathering facts: %s' % e.operation_name)
    except FmcConfigurationError as e:
        module.fail_json(msg='Failed to gather facts because of configuration error: %s' % e.msg)
    except FmcServerError as e:
        module.fail_json(msg='Server returned an error while gathering facts. Status code: %s. '
                         'Server response: %s' % (e.code, e.response))
    except FmcUnexpectedResponse as e:
        module.fail_json(msg='Unexpected response while gathering facts: %s' % e.args[0])
    except ValidationError as e:
        module.fail_json(msg='Validation error while gathering facts: %s' % e.args[0])
    except CheckModeException:
        module.exit_json(changed=False)
    except Exception as e:
        import traceback
        error_details = {
            'error': str(e),
            'type': str(type(e).__name__),
            'traceback': traceback.format_exc()
        }
        module.fail_json(msg='Unexpected error while gathering facts: %s' % str(e), 
                         error_details=error_details)


if __name__ == '__main__':
    main()
