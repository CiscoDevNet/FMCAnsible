# deleteSecurityGroupTag

The deleteSecurityGroupTag operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/securitygrouptags/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/securitygrouptags/{object_id}.md) path.&nbsp;
## Description
**Retrieves the custom security group tag object associated with the specified ID. If no ID is specified, retrieves list of all custom security group tag objects. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Unique identifier of the security group tag object. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'deleteSecurityGroupTag' operation
  cisco.fmcansible.fmc_configuration:
    operation: "deleteSecurityGroupTag"
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```