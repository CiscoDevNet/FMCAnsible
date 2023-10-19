# getAllDeviceLicense

The getAllDeviceLicense operation handles configuration related to [/api/fmc_platform/v1/license/devicelicenses](/paths//api/fmc_platform/v1/license/devicelicenses.md) path.&nbsp;
## Description
**API operations on Device Licenses including: retrieving assigned device licenses, updating the licenses.**

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| filter | False | string <td colspan=3> [DEV ERROR: Missing description] |
| offset | False | integer <td colspan=3> Index of first item to return. |
| limit | False | integer <td colspan=3> Number of items to return. |
| expanded | False | boolean <td colspan=3> If set to true, the GET response displays a list of objects with additional attributes. |

## Example
```yaml
- name: Execute 'getAllDeviceLicense' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getAllDeviceLicense"
    query_params:
        filter: "{{ filter }}"
        offset: "{{ offset }}"
        limit: "{{ limit }}"
        expanded: "{{ expanded }}"

```