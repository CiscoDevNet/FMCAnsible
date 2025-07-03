#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cisco and/or its affiliates.
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

# TODO: remove the need for pre_task in get_access_policies_with_role.yml playbook.
# TODO: Create feature testing for this module to ensure it works as expected.
# TODO: Validate domain UUID to be present and correct in inventory

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'network'}

DOCUMENTATION = """
---
module: fmc_access_policies
short_description: Manages access policies on Cisco FMC devices over REST API
description:
    - Manages access policies on Cisco FMC devices including retrieving all access policies,
      retrieving specific policies, their rules, and associated objects.
    - This module focuses on access policy operations to simplify the retrieval of complex nested structures.
version_added: "2.0.0"
author: "Cisco Systems (@cisco)"

options:
    operation:
        description:
            - The name of the operation to execute. Available operations include 'getAllAccessPolicies',
              'getAccessPolicy', 'getAllAccessRules', 'getAccessRule'
        required: true
        type: str
        choices: ['getAllAccessPolicies', 'getAccessPolicy', 'getAllAccessRules', 'getAccessRule', 'getNestedObjects']
    policy_id:
        description:
            - ID of the access policy to retrieve when using getAccessPolicy or getAllAccessRules operations.
        type: str
    rule_id:
        description:
            - ID of the access rule to retrieve when using getAccessRule operation.
        type: str
    object_type:
        description:
            - Type of objects to retrieve when using getNestedObjects operation.
        type: str
        choices: ['sourceNetworks', 'destinationNetworks', 'sourcePorts', 'destinationPorts', 'applications', 'urls']
    domain_uuid:
        description:
            - Domain UUID of the FMC.
            - This is required for all operations.
        required: true
        type: str
    depth:
        description:
            - The depth level for nested object retrieval, controlling how many levels of nesting to process.
            - Default is 1, meaning only direct objects are retrieved.
        type: int
        default: 1
    output_dir:
        description:
            - Directory where JSON output files will be saved when using the module in a playbook.
            - The module will automatically create this directory if it doesn't exist.
        type: str
        default: "."
    register_as:
        description:
            - Specifies Ansible fact name that is used to register received response from the FMC device.
        type: str
    expanded:
        description:
            - When set to True, returns detailed information for all retrieved objects.
        type: bool
        default: False
"""

EXAMPLES = """
- name: Get all access policies
  fmc_access_policies:
    operation: getAllAccessPolicies
    register_as: access_policies

- name: Get specific access policy
  fmc_access_policies:
    operation: getAccessPolicy
    policy_id: "{{ access_policies[0].id }}"
    register_as: access_policy

- name: Get all access rules for a policy with expanded information
  fmc_access_policies:
    operation: getAllAccessRules
    policy_id: "{{ access_policies[0].id }}"
    expanded: true
    register_as: access_rules

- name: Get all objects for a specific rule with depth=2 (retrieves nested objects)
  fmc_access_policies:
    operation: getNestedObjects
    policy_id: "{{ access_policies[0].id }}"
    rule_id: "{{ access_rules[0].id }}"
    object_type: sourceNetworks
    depth: 2
    register_as: source_networks
"""

RETURN = """
response:
    description: HTTP response returned from the API call.
    returned: success
    type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
import os

from ansible_collections.cisco.fmcansible.plugins.module_utils.configuration import BaseConfigurationResource, CheckModeException, FmcInvalidOperationNameError
from ansible_collections.cisco.fmcansible.plugins.module_utils.fmc_swagger_client import ValidationError
from ansible_collections.cisco.fmcansible.plugins.module_utils.common import construct_ansible_facts, FmcConfigurationError, \
    FmcServerError, FmcUnexpectedResponse


def main():
    fields = dict(
        operation=dict(
            type='str',
            required=True,
            choices=['getAllAccessPolicies', 'getAccessPolicy', 'getAllAccessRules', 'getAccessRule', 'getNestedObjects']
        ),
        policy_id=dict(type='str'),
        rule_id=dict(type='str'),
        object_type=dict(
            type='str',
            choices=['sourceNetworks', 'destinationNetworks', 'sourcePorts', 'destinationPorts', 'applications', 'urls']
        ),
        domain_uuid=dict(type='str', required=True),
        depth=dict(type='int', default=1),
        output_dir=dict(type='str', default="."),
        register_as=dict(type='str'),
        expanded=dict(type='bool', default=False)
    )

    # Define module validation requirements
    required_if = [
        ['operation', 'getAccessPolicy', ['policy_id']],
        ['operation', 'getAllAccessRules', ['policy_id']],
        ['operation', 'getAccessRule', ['policy_id', 'rule_id']],
        ['operation', 'getNestedObjects', ['policy_id', 'rule_id', 'object_type']]
    ]

    module = AnsibleModule(
        argument_spec=fields,
        required_if=required_if,
        supports_check_mode=True
    )
    params = module.params

    connection = Connection(module._socket_path)
    resource = BaseConfigurationResource(connection, module.check_mode)

    # Use domain_uuid provided directly to the module
    domain_uuid = params['domain_uuid']
    if not domain_uuid:
        module.fail_json(msg="domain_uuid is required")

    operation = params['operation']
    query_params = {}
    path_params = {'domainUUID': domain_uuid}  # Add domain_uuid to path_params for all operations

    # Build appropriate query and path parameters based on operation
    if operation == 'getAllAccessPolicies':
        # Map to the existing operation in the FMC API
        actual_operation = 'getAllAccessPolicies'
        if params['expanded']:
            query_params['expanded'] = 'true'

    elif operation == 'getAccessPolicy':
        # Map to the existing operation in the FMC API
        actual_operation = 'getAccessPolicy'
        path_params['objectId'] = params['policy_id']

    elif operation == 'getAllAccessRules':
        # Map to the existing operation in the FMC API
        actual_operation = 'getAllAccessRules'
        path_params['containerUUID'] = params['policy_id']
        if params['expanded']:
            query_params['expanded'] = 'true'

    elif operation == 'getAccessRule':
        # Map to the existing operation in the FMC API
        actual_operation = 'getAccessRule'
        path_params['containerUUID'] = params['policy_id']
        path_params['objectId'] = params['rule_id']

    elif operation == 'getNestedObjects':
        # This is a custom operation that will use multiple API calls
        # First, get the access rule
        actual_operation = 'getAccessRule'
        path_params['containerUUID'] = params['policy_id']
        path_params['objectId'] = params['rule_id']

    # Prepare parameters for the API call
    api_params = {
        'operation': actual_operation,
        'path_params': path_params,
        'query_params': query_params
    }

    if params['register_as']:
        api_params['register_as'] = params['register_as']

    try:
        # Execute the API operation
        resp = resource.execute_operation(actual_operation, api_params)

        # For getNestedObjects, we need to do additional processing
        if operation == 'getNestedObjects' and resp:
            object_type = params['object_type']
            depth = params['depth']

            # If the requested object type exists in the rule
            if object_type in resp and 'objects' in resp[object_type]:
                objects_list = resp[object_type]['objects']

                # If depth > 1, retrieve each nested object
                if depth > 1 and objects_list:
                    enriched_objects = []
                    for obj in objects_list:
                        # Get detailed object information
                        obj_type = obj.get('type', '')
                        # Determine the appropriate operation based on object type
                        if obj_type.lower() == 'networkgroup' or obj_type.lower() == 'networkobject':
                            get_obj_operation = 'getNetworkObject'
                        elif obj_type.lower().endswith('networks'):
                            get_obj_operation = 'getNetworkObject'
                        elif obj_type.lower() == 'protocolportobject' or obj_type.lower().endswith('portobject'):
                            get_obj_operation = 'getPortObject'
                        elif obj_type.lower().endswith('ports'):
                            get_obj_operation = 'getPortObject'
                        elif obj_type.lower().endswith('urls'):
                            get_obj_operation = 'getUrlObject'
                        elif obj_type.lower().endswith('applications'):
                            get_obj_operation = 'getApplicationObject'
                        else:
                            # Default to a generic operation for unknown types
                            get_obj_operation = 'getAllAccessPolicies'  # Using a known valid operation
                            module.warn(f"Unknown object type: {obj_type}. Cannot retrieve details.")
                            enriched_objects.append(obj)
                            continue

                        obj_params = {
                            'operation': get_obj_operation,
                            'path_params': {
                                'objectId': obj['id'],
                                'domainUUID': domain_uuid
                            }
                        }
                        try:
                            obj_details = resource.execute_operation(get_obj_operation, obj_params)
                            enriched_objects.append(obj_details)
                        except (FmcConfigurationError, FmcServerError) as e:
                            # If we can't get details, use the original object and provide a helpful warning
                            if hasattr(e, 'code') and e.code == 404:
                                module.warn(f"Object not found: {obj['id']} (Type: {obj_type}). "
                                            f"This object may have been deleted but is still referenced in the rule.")
                            else:
                                module.warn(f"Could not retrieve details for object {obj['id']} (Type: {obj_type}): {str(e)}")
                            # Add whatever information we do have about the object
                            enriched_objects.append(obj)
                        except (FmcUnexpectedResponse, ValidationError) as e:
                            module.warn(f"Error processing object {obj['id']} (Type: {obj_type}): {str(e)}")
                            enriched_objects.append(obj)

                    # Replace the response with the enriched objects
                    resp = {'objects': enriched_objects}
                else:
                    resp = {'objects': objects_list}
            else:
                resp = {'objects': []}

        # Handle output_dir parameter - save response to a file
        output_dir = params['output_dir']
        if output_dir:
            # Ensure the output directory exists
            os.makedirs(output_dir, exist_ok=True)

            # Define the output file path
            output_file = os.path.join(output_dir, 'fmc_access_policy_response.json')

            # Write the response to the file
            with open(output_file, 'w') as f:
                import json
                json.dump(resp, f, indent=4)

            module.exit_json(changed=False,
                             response=resp,
                             ansible_facts=construct_ansible_facts(resp, module.params),
                             output_file=output_file)
        else:
            module.exit_json(changed=False,
                             response=resp,
                             ansible_facts=construct_ansible_facts(resp, module.params))

    except FmcInvalidOperationNameError as e:
        module.fail_json(msg='Invalid operation name provided: %s' % e.operation_name)
    except FmcConfigurationError as e:
        module.fail_json(msg='Failed to execute %s operation because of the configuration error: %s' % (operation, e.msg))
    except FmcServerError as e:
        module.fail_json(msg='Server returned an error trying to execute %s operation. Status code: %s. '
                         'Server response: %s' % (operation, e.code, e.response))
    except FmcUnexpectedResponse as e:
        module.fail_json(msg=e.args[0])
    except ValidationError as e:
        module.fail_json(msg=e.args[0])
    except CheckModeException:
        module.exit_json(changed=False)


if __name__ == '__main__':
    main()
