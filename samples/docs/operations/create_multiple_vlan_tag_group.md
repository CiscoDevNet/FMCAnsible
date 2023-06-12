# createMultipleVlanTagGroup

The createMultipleVlanTagGroup operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/vlangrouptags](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/vlangrouptags.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the vlan group tag objects associated with the specified ID. If no ID is specified for a GET, retrieves list of all vlan group tag objects. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value | Description |
| --------- | -------- | -------- |
| name | vlangroup_obj_1 | User assigned resource name. |
| objects | [{'data': {'startTag': 'valid_tag', 'endTag': 'valid_tag', 'type': 'VlanTagLiteral'}, 'type': 'VlanTag', 'name': 'Tag1', 'id': 'vlantagObjectUUID'}] | List of member vlan tags in this group |
| literals | [{'type': 'VlanTagLiteral', 'startTag': 'valid_tag', 'endTag': 'valid_tag'}] | List of tag values in group. |
| type | VlanGroupTag | Type associated with resource: VlanTagGroup. |
| description | description_about_group | User provided resource description. |
| overridable | true/false | Boolean indicating whether object values can be overridden. |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string | Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| bulk | False | boolean | Enables bulk create for vlan group tags. |

## Example
```yaml
- name: Execute 'createMultipleVlanTagGroup' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createMultipleVlanTagGroup"
    data:
        name: "vlangroup_obj_1"
        objects: [{'data': {'startTag': 'valid_tag', 'endTag': 'valid_tag', 'type': 'VlanTagLiteral'}, 'type': 'VlanTag', 'name': 'Tag1', 'id': 'vlantagObjectUUID'}]
        literals: [{'type': 'VlanTagLiteral', 'startTag': 'valid_tag', 'endTag': 'valid_tag'}]
        type: "VlanGroupTag"
        description: "description_about_group"
        overridable: "true/false"
    path_params:
        domainUUID: "{{ domain_uuid }}"
    query_params:
        bulk: "{{ bulk }}"

```
