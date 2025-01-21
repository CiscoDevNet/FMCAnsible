# getAllBackupFile

The getAllBackupFile operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/backup/files](/paths//api/fmc_config/v1/domain/{domain_uuid}/backup/files.md) path.&nbsp;
## Description
**Retrieves or deletes the backup associated with the specified UUID(In case of FMC manager identifier should be entered in place of UUID). <br/>If no filter is specified for a GET, DELETE retrieves the latest backup.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| offset | False | integer <td colspan=3> Index of first item to return. |
| limit | False | integer <td colspan=3> Number of items to return. |
| expanded | False | boolean <td colspan=3> If set to true, the GET response displays a list of objects with additional attributes. |

## Example
```yaml
- name: Execute 'getAllBackupFile' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getAllBackupFile"
    path_params:
        domainUUID: "{{ domain_uuid }}"
    query_params:
        offset: "{{ offset }}"
        limit: "{{ limit }}"
        expanded: "{{ expanded }}"

```