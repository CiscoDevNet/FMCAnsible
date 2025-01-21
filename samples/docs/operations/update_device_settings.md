# updateDeviceSettings

The updateDeviceSettings operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/devices/devicesettings/{containerUUID}](/paths//api/fmc_config/v1/domain/{domain_uuid}/devices/devicesettings/{container_uuid}.md) path.&nbsp;
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
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'updateDeviceSettings' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateDeviceSettings"
    data:
        id: deviceUUID
        type: DeviceSettings
        deploymentSettings: {'enableAutoRollback': True, 'rollbackConnectivityMonitorInterval': 80}
    path_params:
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```