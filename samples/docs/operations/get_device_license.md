# getDeviceLicense

The getDeviceLicense operation handles configuration related to [/api/fmc_platform/v1/license/devicelicenses/{objectId}](/paths//api/fmc_platform/v1/license/devicelicenses/{object_id}.md) path.&nbsp;
## Description
**API operations on Device Licenses including: retrieving assigned device licenses, updating the licenses.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> [DEV ERROR: Missing description] |

## Example
```yaml
- name: Execute 'getDeviceLicense' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getDeviceLicense"
    path_params:
        objectId: "{{ object_id }}"

```