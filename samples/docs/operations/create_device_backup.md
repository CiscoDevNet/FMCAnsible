# createDeviceBackup

The createDeviceBackup operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/backup/operational/devicebackup](/paths//api/fmc_config/v1/domain/{domain_uuid}/backup/operational/devicebackup.md) path.&nbsp;
## Description
**Creates the backup associated with the specified UUID. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createDeviceBackup' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createDeviceBackup"
    path_params:
        domainUUID: "{{ domain_uuid }}"

```