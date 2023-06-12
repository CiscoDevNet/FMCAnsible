# createPolicyList

The createPolicyList operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/policylists](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/policylists.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the PolicyList object associated with the specified ID. If no ID is specified for a GET, retrieves list of all PolicyList objects. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value | Description |
| --------- | -------- | ----------- |
| interfaces | [{'name': 'secZone', 'id': 'security-zone-uuid', 'type': 'SecurityZone'}] | Add the Security zones/Interface groups that contain the interfaces through which the device communicates with the management station |
| interfaceNames | ['inside'] | Interface logical names associated with this object |
| extendedCommunityLists | [{'name': 'ext_com_1', 'id': 'ext_com_uuid', 'type': 'ExtendedCommunityList'}] | The route can match this extendedcommunity |
| tag | 2211 | This setting allows you to match any routes that have a specified security group tag. The tag values can range from 0 to 4294967295 |
| matchCommunityExactly | False | Match the BGP community exactly with the specified community |
| metric | 111 | This setting allows you to match any routes that have a specified metric. The metric values can range from 0 to 4294967295. |
| name | GlobalPL123 | Name for the policy list object |
| action | DENY (DEFAULT), PERMIT | Action to take for this matching criteria: PERMIT or DENY |
| overridable | False | Defines the override details for this object.  |
| description |   |  A policy list for use in a route map for Border Gateway Protocol (BGP).  |
| type | PolicyList | PolicyList - type of this object |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string | Domain UUID |

## Example
```yaml
- name: Execute 'createPolicyList' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createPolicyList"
    data:
        interfaces: [{'name': 'secZone', 'id': 'security-zone-uuid', 'type': 'SecurityZone'}]
        interfaceNames: ['inside']
        extendedCommunityLists: [{'name': 'ext_com_1', 'id': 'ext_com_uuid', 'type': 'ExtendedCommunityList'}]
        tag: 2211
        matchCommunityExactly: False
        metric: 111
        name: "GlobalPL123"
        action: "DENY"
        overridable: False
        description: " "
        type: "PolicyList"
    path_params:
        domainUUID: "{{ domain_uuid }}"

```
