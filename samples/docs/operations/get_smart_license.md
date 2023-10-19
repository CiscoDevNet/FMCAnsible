# getSmartLicense

The getSmartLicense operation handles configuration related to [/api/fmc_platform/v1/license/smartlicenses](/paths//api/fmc_platform/v1/license/smartlicenses.md) path.&nbsp;
## Description
**API operations on Smart Licenses including: retrieving registration status, requesting license registration, de-registering Smart Licenses and activating evaluation mode. **

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| offset | False | integer <td colspan=3> Index of first item to return. |
| limit | False | integer <td colspan=3> Number of items to return. |
| expanded | False | boolean <td colspan=3> If set to true, the GET response displays a list of objects with additional attributes. |

## Example
```yaml
- name: Execute 'getSmartLicense' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getSmartLicense"
    query_params:
        offset: "{{ offset }}"
        limit: "{{ limit }}"
        expanded: "{{ expanded }}"

```