# updateMultipleDeviceSettings

The updateMultipleDeviceSettings operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/devices/devicesettings](/paths//api/fmc_config/v1/domain/{domain_uuid}/devices/devicesettings.md) path.&nbsp;
## Description
**Retrieves or modifies the Device Settings. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| id | deviceUUID |
| type | DeviceSettings |
| deploymentSettings | {'enableAutoRollback': True, 'rollbackConnectivityMonitorInterval': 80} |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| bulk | True | boolean <td colspan=3> Enables bulk update on device settings. |

## Example
```yaml
- name: Execute 'updateMultipleDeviceSettings' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateMultipleDeviceSettings"
    data:
        id: deviceUUID
        type: DeviceSettings
        deploymentSettings: {'enableAutoRollback': True, 'rollbackConnectivityMonitorInterval': 80}
    path_params:
        domainUUID: "{{ domain_uuid }}"
    query_params:
        bulk: "{{ bulk }}"

```