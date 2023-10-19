# getHealthPolicy

The getHealthPolicy operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/healthpolicies/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/healthpolicies/{object_id}.md) path.&nbsp;
## Description
**Retrieves the Health Policy with the associated ID. If no ID is specified, retrieves a list of all Health Policies.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Unique identifier of a Health policy. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'getHealthPolicy' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getHealthPolicy"
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```