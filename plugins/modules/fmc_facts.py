#!/usr/bin/python

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
short_description: Gather facts about FMC devices
description:
    - This module provides a way to gather facts about FMC devices and their configurations.
version_added: "1.0.0"
author: "Cisco Systems (@cisco)"

options:
    gather_subset:
        description:
            - When supplied, this argument will restrict the facts collected to a given subset.
        required: false
        default: ['min']
        type: list
        elements: str
        choices: ['all', 'min', 'domains', 'devices', 'access_policies',
                  'file_policies', 'intrusion_policies', 'physical_interfaces',
                  'network_objects', 'port_objects', 'security_zones', 'device_groups']
    domain_uuid:
        description:
            - UUID of the domain to gather facts for.
        required: false
        type: str
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

# Gather file and intrusion policies
- name: Gather file and intrusion policies
  cisco.fmcansible.fmc_facts:
    gather_subset:
      - domains
      - file_policies
      - intrusion_policies

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
"""

import traceback

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.cisco.fmcansible.plugins.module_utils.common import (
    FmcConfigurationError, FmcServerError, FmcUnexpectedResponse)
from ansible_collections.cisco.fmcansible.plugins.module_utils.configuration import (
    BaseConfigurationResource, CheckModeException,
    FmcInvalidOperationNameError)
from ansible_collections.cisco.fmcansible.plugins.module_utils.facts import \
    FmcFactsBase
from ansible_collections.cisco.fmcansible.plugins.module_utils.fmc_swagger_client import \
    ValidationError


def main():
    argument_spec = {
        'gather_subset': {
            'type': 'list',
            'elements': 'str',
            'default': ['min'],  # Changed default to 'min' for performance
            'choices': ['all', 'min', 'domains', 'devices', 'access_policies',
                        'file_policies', 'intrusion_policies', 'physical_interfaces',
                        'network_objects', 'port_objects', 'security_zones',
                        'device_groups']
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

    try:
        # Use the facts gathering class
        facts_gatherer = FmcFactsBase(resource)
        facts = facts_gatherer.gather_facts(gather_subset, domain_uuid)

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
        error_details = {
            'error': str(e),
            'type': str(type(e).__name__),
            'traceback': traceback.format_exc()
        }
        module.fail_json(msg='Unexpected error while gathering facts: %s' % str(e),
                         error_details=error_details)


if __name__ == '__main__':
    main()
