# getFlexConfig

The getFlexConfig operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/flexconfigpolicies/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/flexconfigpolicies/{object_id}.md) path.&nbsp;
## Description
**Retrieves the FlexConfig Policy with the associated ID. If no ID is specified, retrieves a list of all FlexConfig Policies.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Unique identifier of a FlexConfig Policy. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'getFlexConfig' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getFlexConfig"
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```