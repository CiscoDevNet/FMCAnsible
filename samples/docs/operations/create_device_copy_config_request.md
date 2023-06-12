# createDeviceCopyConfigRequest

The createDeviceCopyConfigRequest operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/devices/copyconfigrequests](/paths//api/fmc_config/v1/domain/{domain_uuid}/devices/copyconfigrequests.md) path.&nbsp;
## Description
**Copy configuration operation on device. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value | Description |
| --------- | -------- | ----------- |
| sourceDevice | {'id': 'device_uuid', 'type': 'Device'} | Unique ID of the device. |
| targetDeviceList | [{'id': 'device_uuid', 'type': 'Device'}] | Target device list is a standalone device UUID |
| copySharedPolicies | False | Boolean value. Copies shared policies from source standalone device or HA to target standalone device based on True or False input |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string | Domain UUID |

## Example
```yaml
- name: Execute 'createDeviceCopyConfigRequest' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createDeviceCopyConfigRequest"
    data:
        sourceDevice: {'id': 'device_uuid', 'type': 'Device'}
        targetDeviceList: [{'id': 'device_uuid', 'type': 'Device'}]
        copySharedPolicies: False
    path_params:
        domainUUID: "{{ domain_uuid }}"

```
