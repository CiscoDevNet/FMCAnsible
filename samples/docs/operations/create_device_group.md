# createDeviceGroup

The createDeviceGroup operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/devicegroups/devicegrouprecords](/paths//api/fmc_config/v1/domain/{domain_uuid}/devicegroups/devicegrouprecords.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the device group associated with the specified ID. If no ID is specified for a GET, retrieves list of all device groups. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value | Description |
| --------- | -------- | -------- |
| name | zoom | User assigned resource name. |
| type | DeviceGroup | Response object associated with resource: DeviceGroup. |
| members | [{'id': 'deviceUUID', 'type': 'Device', 'name': 'deviceName'}] | Represents devices included in group. |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string | Domain UUID |

## Example
```yaml
- name: Execute 'createDeviceGroup' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createDeviceGroup"
    data:
        name: "zoom"
        type: "DeviceGroup"
        members: [{'id': 'deviceUUID', 'type': 'Device', 'name': 'deviceName'}]
    path_params:
        domainUUID: "{{ domain_uuid }}"

```
