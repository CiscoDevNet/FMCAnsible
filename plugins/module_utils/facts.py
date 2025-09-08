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

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection

from .configuration import BaseConfigurationResource


class FmcFactsBase(object):
    """Base class for FMC fact gathering"""
    
    def __init__(self, module):
        self.module = module
        self.connection = Connection(module._socket_path)
        self.resource = BaseConfigurationResource(self.connection, False)  # Never use check mode for facts
        
    def gather_all_facts(self):
        """Gather all available FMC facts"""
        facts = {'fmc': {}}
        
        # Gather domains first
        domains = self._gather_domains()
        facts['fmc']['domains'] = domains
        
        # Gather facts for each domain
        if domains:
            facts['fmc']['devices'] = {}
            facts['fmc']['access_policies'] = {}
            facts['fmc']['network_objects'] = {}
            facts['fmc']['port_objects'] = {}
            facts['fmc']['security_zones'] = {}
            
            for domain in domains:
                domain_id = domain.get('uuid')
                if domain_id:
                    facts['fmc']['devices'][domain_id] = self._gather_devices(domain_id)
                    facts['fmc']['access_policies'][domain_id] = self._gather_access_policies(domain_id)
                    facts['fmc']['network_objects'][domain_id] = self._gather_network_objects(domain_id)
                    facts['fmc']['port_objects'][domain_id] = self._gather_port_objects(domain_id)
                    facts['fmc']['security_zones'][domain_id] = self._gather_security_zones(domain_id)
        
        return facts
    
    def _gather_domains(self):
        """Gather domain information"""
        try:
            return self.resource.execute_operation('getAllDomain', {})
        except Exception:
            return []
    
    def _gather_devices(self, domain_uuid):
        """Gather device information for a domain"""
        try:
            params = {'path_params': {'domainUUID': domain_uuid}}
            return self.resource.execute_operation('getAllDevice', params)
        except Exception:
            return []
    
    def _gather_access_policies(self, domain_uuid):
        """Gather access policy information for a domain"""
        try:
            params = {'path_params': {'domainUUID': domain_uuid}}
            return self.resource.execute_operation('getAllAccessPolicy', params)
        except Exception:
            return []
    
    def _gather_network_objects(self, domain_uuid):
        """Gather network object information for a domain"""
        try:
            params = {'path_params': {'domainUUID': domain_uuid}}
            return self.resource.execute_operation('getAllNetworkObject', params)
        except Exception:
            return []
    
    def _gather_port_objects(self, domain_uuid):
        """Gather port object information for a domain"""
        try:
            params = {'path_params': {'domainUUID': domain_uuid}}
            return self.resource.execute_operation('getAllPortObject', params)
        except Exception:
            return []
    
    def _gather_security_zones(self, domain_uuid):
        """Gather security zone information for a domain"""
        try:
            params = {'path_params': {'domainUUID': domain_uuid}}
            return self.resource.execute_operation('getAllSecurityZoneObject', params)
        except Exception:
            return []


def get_fmc_facts(module):
    """Main entry point for gathering FMC facts"""
    fmc_facts = FmcFactsBase(module)
    return fmc_facts.gather_all_facts()
