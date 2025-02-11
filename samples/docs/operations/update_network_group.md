# updateNetworkGroup

The updateNetworkGroup operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/networkgroups/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/networkgroups/{object_id}.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the network group object associated with the specified ID. If no ID is specified for a GET, retrieves list of all network group objects. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| id | networkGroup1UUID |
| name | networkgroup_obj1_updated |
| type | NetworkGroup |
| objects | [{'type': 'Network', 'id': 'NetworkObjectUUID'}, {'type': 'Host', 'id': 'HostObjectUUID'}, {'type': 'Range', 'id': 'RangeObjectUUID'}] |
| literals | [{'type': 'Network', 'value': '1.2.3.0/24'}, {'type': 'Host', 'value': '1.2.3.4'}] |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier for a network group. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| action | False | string <td colspan=3> This parameter specifies that the network objects will be added or removed from the network group. This parameter is a string. When its value is add the PUT operation will add these network objects to the network group, and if the value is remove the PUT operation will remove these network objects from the network group. |

## Example
```yaml
- name: Execute 'updateNetworkGroup' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateNetworkGroup"
    data:
        id: networkGroup1UUID
        name: networkgroup_obj1_updated
        type: NetworkGroup
        objects: [{'type': 'Network', 'id': 'NetworkObjectUUID'}, {'type': 'Host', 'id': 'HostObjectUUID'}, {'type': 'Range', 'id': 'RangeObjectUUID'}]
        literals: [{'type': 'Network', 'value': '1.2.3.0/24'}, {'type': 'Host', 'value': '1.2.3.4'}]
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"
    query_params:
        action: "{{ action }}"

```