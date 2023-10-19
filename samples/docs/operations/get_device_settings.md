# getDeviceSettings

The getDeviceSettings operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/devices/devicesettings/{containerUUID}](/paths//api/fmc_config/v1/domain/{domain_uuid}/devices/devicesettings/{container_uuid}.md) path.&nbsp;
## Description
**Retrieves or modifies the Device Settings.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'getDeviceSettings' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getDeviceSettings"
    path_params:
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```