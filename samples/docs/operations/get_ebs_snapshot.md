# getEBSSnapshot

The getEBSSnapshot operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/integration/ebssnapshot/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/integration/ebssnapshot/{object_id}.md) path.&nbsp;
## Description
**Retrieves or creates an EBS snapshot.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> The id of the snapshot. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'getEBSSnapshot' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getEBSSnapshot"
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```