# createAccessPolicy

The createAccessPolicy operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/accesspolicies.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the access control policy associated with the specified ID. Also, retrieves list of all access control policies. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value | Description |
| --------- | -------- | ----------- |
| type | AccessPolicy | Type of the access control policy; this value is always AccessPolicy. |
| name | AccessPolicy1 | User-specified name of the access control policy. |
| defaultAction | {'action': 'BLOCK'} | Specifies the action to take when the conditions defined by the rule are met. One of: BLOCK / TRUST / NETWORK_DISCOVERY / PERMIT / INHERIT_FROM_PARENT. |


## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string | Domain UUID |

## Example
```yaml
- name: Execute 'createAccessPolicy' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createAccessPolicy"
    data:
        type: "AccessPolicy"
        name: "AccessPolicy1"
        defaultAction: {'action': 'BLOCK'}
    path_params:
        domainUUID: "{{ domain_uuid }}"

```
