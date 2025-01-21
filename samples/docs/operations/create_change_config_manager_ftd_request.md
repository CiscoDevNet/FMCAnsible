# createChangeConfigManagerFTDRequest

The createChangeConfigManagerFTDRequest operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/devices/operational/changemanagers](/paths//api/fmc_config/v1/domain/{domain_uuid}/devices/operational/changemanagers.md) path.&nbsp;
## Description
**APIs to support migrating configuration management of FTD from FMC to CDO _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| type | ChangeManager |
| action | CONFIGURE_DEVICE_VALIDATE |
| configManagerHost | fmc.cdo.com |
| deviceList | [{'id': '1087edc2-064c-4fa7-90b9-72ae7ed4c474'}, {'id': '3a6bda97-5f7c-4874-934c-01ca2095b780'}] |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createChangeConfigManagerFTDRequest' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createChangeConfigManagerFTDRequest"
    data:
        type: ChangeManager
        action: CONFIGURE_DEVICE_VALIDATE
        configManagerHost: fmc.cdo.com
        deviceList: [{'id': '1087edc2-064c-4fa7-90b9-72ae7ed4c474'}, {'id': '3a6bda97-5f7c-4874-934c-01ca2095b780'}]
    path_params:
        domainUUID: "{{ domain_uuid }}"

```