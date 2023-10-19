# updateMultipleDeviceLicense

The updateMultipleDeviceLicense operation handles configuration related to [/api/fmc_platform/v1/license/devicelicenses](/paths//api/fmc_platform/v1/license/devicelicenses.md) path.&nbsp;
## Description
**API operations on Device Licenses including: retrieving assigned device licenses, updating the licenses. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| type | DeviceLicense |
| id | bdeb61ba-50d3-11ec-9058-8c269f48f8b7 |
| licenseTypes | ['IPS', 'MALWARE_DEFENSE'] |
| performanceTier | FTDv50 |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| bulk | True | boolean <td colspan=3> [DEV ERROR: Missing description] |

## Example
```yaml
- name: Execute 'updateMultipleDeviceLicense' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateMultipleDeviceLicense"
    data:
        type: DeviceLicense
        id: bdeb61ba-50d3-11ec-9058-8c269f48f8b7
        licenseTypes: ['IPS', 'MALWARE_DEFENSE']
        performanceTier: FTDv50
    query_params:
        bulk: "{{ bulk }}"

```