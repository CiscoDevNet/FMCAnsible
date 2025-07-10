# Cisco FMC Ansible

## Table of Contents
- [FMC Configuration Module](#fmc-configuration-module)
  - [Operations](#operations)
  - [Parameters](#parameters)
  - [Examples](#examples)
    - [Creating a Network Object](#creating-a-network-object)
    - [Deleting a Network Object](#deleting-a-network-object)
    - [Getting All Access Policies](#getting-all-access-policies)
    - [Getting Access Rules for a Policy](#getting-access-rules-for-a-policy)
- [FMC Access Policies Module](#fmc-access-policies-module)
  - [Operations](#operations-1)
  - [Parameters](#parameters-1)
- [Cache Module](#cache-module)
  - [Usage](#usage)
  - [Methods](#methods)
- [Get Access Policies Role](#get-access-policies-role)
  - [Role Variables](#role-variables)
  - [Example Usage](#example-usage)



## FMC Configuration Module

The `fmc_configuration` module is a general-purpose module for managing configuration on Cisco FMC devices over the REST API. It allows for creating, updating, removing configuration objects, scheduling jobs, deploying pending changes, and more.

### Operations

Operations typically start with verbs like:
- `add` - Create new objects
- `edit` - Update existing objects
- `get` - Retrieve objects
- `upsert` - Create or update objects
- `delete` - Remove objects

### Parameters

- `operation` (required) - The name of the operation to execute
- `data` - JSON-like object or array sent as body parameters in a REST API call
- `query_params` - Key-value pairs sent as query parameters
- `path_params` - Key-value pairs sent as path parameters
- `register_as` - Ansible fact name used to register the response
- `filters` - Key-value dict representing equality filters

### Examples

#### Creating a Network Object

```yaml
- name: Create a network object
  fmc_configuration:
    operation: addNetworkObject
    data:
      name: Ansible-network-host
      description: From Ansible with love
      subType: HOST
      value: 192.168.2.0
      dnsResolution: IPV4_AND_IPV6
      type: networkobject
      isSystemDefined: false
    register_as: hostNetwork
```

#### Deleting a Network Object

```yaml
- name: Delete the network object
  fmc_configuration:
    operation: deleteNetworkObject
    path_params:
      objId: "{{ hostNetwork['id'] }}"
```

#### Getting All Access Policies

```yaml
- name: Get all access policies
  fmc_configuration:
    operation: getAllAccessPolicies
    register_as: access_policies
```

#### Getting Access Rules for a Policy

```yaml
- name: Get access rules for a policy
  fmc_configuration:
    operation: getAllAccessRules
    path_params:
      containerUUID: "{{ access_policies[0].id }}"
    register_as: access_rules
```
## FMC Access Policies Module

The new `fmc_access_policies` module provides the following operations:

- `getAllAccessPolicies` - Retrieves all access policies from FMC
- `getAccessPolicy` - Gets a specific access policy by ID
- `getAllAccessRules` - Gets all access rules for a specific policy
- `getAccessRule` - Gets a specific access rule by ID
- `getNestedObjects` - Gets objects (like networks, ports) referenced in a rule with the ability to specify a nesting depth

### Parameters

The module includes several parameters to customize your queries:

- `policy_id` - ID of the access policy to work with
- `rule_id` - ID of the access rule to retrieve
- `object_type` - Type of objects to retrieve (sourceNetworks, destinationNetworks, etc.)
- `depth` - Controls how deep to go when retrieving nested objects
- `expanded` - When set to True, returns detailed information for objects
- `register_as` - Specifies the Ansible fact name to register the response as

## Cache Module

The `cache.py` module provides a file-based cache system for storing FMC API responses to reduce redundant API calls during playbook execution.

### Usage

The cache module is used internally by other modules to improve performance, particularly when retrieving large amounts of data from FMC.

```python
from ansible_collections.cisco.fmcansible.plugins.module_utils.cache import ResponseCache

# Initialize cache with a file path
cache = ResponseCache('/path/to/cache_file.json')

# Cache a response
cache.cache_response('policy_rules', rules_data, 'fmc.example.com')

# Retrieve cached responses
cached_data = cache.get_cached_responses('fmc.example.com')
```

### Methods

- `cache_response(name, response_body, host)` - Cache a response with a specific name for a given host
- `get_cached_responses(host)` - Get all cached responses for a specific host
- `clear()` - Clear the cache

## Get Access Policies Role

A pre-built Ansible role for collecting and processing access policies from Cisco FMC.

### Role Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `domain_uuid` | UUID of the FMC domain to use | Required |
| `output_dir` | Directory where JSON output files will be saved | `.` (current directory) |
| `object_depth` | How deep to retrieve nested objects | `2` |
| `collect_ports` | Whether to collect port objects | `true` |

### Example Usage

```yaml
- name: Collect FMC Access Policies and Rules
  hosts: fmc
  gather_facts: no
  connection: httpapi
  collections:
    - cisco.fmcansible
  vars:
    domain_uuid: "your-domain-uuid-here"
    output_dir: "/tmp/fmc_policies"
    
  pre_tasks:
    - name: Ensure output directory exists
      file:
        path: "{{ output_dir }}"
        state: directory
      delegate_to: localhost
      run_once: true
      
  roles:
    - role: get_access_policies
```
