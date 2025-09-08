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

from ansible.plugins.action import ActionBase
from ansible.utils.display import Display

display = Display()


class ActionModule(ActionBase):
    """
    Custom action plugin for FMC facts gathering.
    This plugin is called when gather_facts: true is used with httpapi connection type 'fmc'.
    It automatically calls the fmc_facts module with optimized settings.
    """

    def run(self, tmp=None, task_vars=None):
        """
        Execute the FMC facts gathering.
        This is called automatically by Ansible when gather_facts: true is used.
        """
        result = super(ActionModule, self).run(tmp, task_vars)
        
        if task_vars is None:
            task_vars = {}

        # Check if we're using an httpapi connection (which FMC uses)
        connection_type = task_vars.get('ansible_connection', 'ssh')
        
        if connection_type == 'httpapi':
            display.vvv("FMC Action Plugin: Detected httpapi connection, gathering FMC facts")
            
            # Get gather_subset from task args or use default 'min' for performance
            gather_subset = self._task.args.get('gather_subset', ['min'])
            domain_uuid = self._task.args.get('domain_uuid', None)
            
            # Prepare module arguments
            module_args = {
                'gather_subset': gather_subset
            }
            if domain_uuid:
                module_args['domain_uuid'] = domain_uuid
            
            # Call our custom fmc_facts module
            facts_result = self._execute_module(
                module_name='cisco.fmcansible.fmc_facts',
                module_args=module_args,
                task_vars=task_vars,
                tmp=tmp
            )
            
            if facts_result.get('failed'):
                result.update(facts_result)
                return result
            
            # Merge the facts into our result
            if 'ansible_facts' in facts_result:
                result['ansible_facts'] = facts_result['ansible_facts']
            
            result['changed'] = False
            display.vvv("FMC Action Plugin: Successfully gathered FMC facts")
        else:
            # For non-httpapi connections, fall back to standard behavior
            display.vvv("FMC Action Plugin: Non-httpapi connection detected, skipping FMC facts")
            result['skipped'] = True
            result['msg'] = 'FMC facts gathering only works with httpapi connections'
        
        return result
