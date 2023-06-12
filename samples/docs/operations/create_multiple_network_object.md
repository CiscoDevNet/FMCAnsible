# createMultipleNetworkObject

The createMultipleNetworkObject operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/networks](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/networks.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the network objects associated with the specified ID. If no ID is specified for a GET, retrieves list of all network objects. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value | Description |
| --------- | -------- | ----------- |
| name | net1 | User assigned resource name. |
| value | 1.0.0.0/24 | Actual value of the network. |
| overridable | False | Boolean indicating whether object values can be overridden. |
| description | Network obj 1 | User provided resource description. |
| type | NetworkObject | Type associated with resource: NetworkObject. |
| name | net2 |  User assigned resource name. | |
| value | 1.1.0.0/24 |  Actual value of the network. |  |
| overridable | False |  Boolean indicating whether object values can be overridden. | |
| description | Network obj 2 | User provided resource description. | |
| type | NetworkObject |  Type associated with resource: NetworkObject. | |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string | Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| bulk | False | boolean | Enables bulk create for network objects. |

## Example
```yaml
- name: Execute 'createMultipleNetworkObject' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createMultipleNetworkObject"
    data:
        name: "net1"
        value: "1.0.0.0/24"
        overridable: False
        description: "Network obj 1"
        type: "NetworkObject"
        name: "net2"
        value: "1.1.0.0/24"
        overridable: False
        description: "Network obj 2"
        type: "NetworkObject"
    path_params:
        domainUUID: "{{ domain_uuid }}"
    query_params:
        bulk: "{{ bulk }}"

```
