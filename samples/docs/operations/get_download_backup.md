# getDownloadBackup

The getDownloadBackup operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/backup/downloadbackup/{targetId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/backup/downloadbackup/{target_id}.md) path.&nbsp;
## Description
**Retrieves the backup associated with the specified UUID(In case of FMC manager identifier should be entered in place of UUID). <br/>If no filter is specified for a GET, retrieves the latest backup.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| targetId | True | string <td colspan=3> Identifier for device/container.<br/>**FMC backup can be located by placing identifier <code>manager</code> instead of UUID. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| backupVersion | False | string <td colspan=3> To be used in locating backup for device/container UUID <code>backupVersion</code>. <br/>**Filter parameter is optional and if not provided the latest backup will be fetched. |

## Example
```yaml
- name: Execute 'getDownloadBackup' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getDownloadBackup"
    path_params:
        targetId: "{{ target_id }}"
        domainUUID: "{{ domain_uuid }}"
    query_params:
        backupVersion: "{{ backup_version }}"

```