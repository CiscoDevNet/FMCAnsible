# getInternalCA

The getInternalCA operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/internalcas/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/internalcas/{object_id}.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the Internal CA associated with the specified ID. If no ID is specified, retrieves list of all Internal CAs.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Unique identifier of an Internal CA. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'getInternalCA' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getInternalCA"
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```