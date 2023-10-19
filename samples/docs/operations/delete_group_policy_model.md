# deleteGroupPolicyModel

The deleteGroupPolicyModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/grouppolicies/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/grouppolicies/{object_id}.md) path.&nbsp;
## Description
**Defines  the group policies for VPN _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Unique identifier of the Group policy. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'deleteGroupPolicyModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "deleteGroupPolicyModel"
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```