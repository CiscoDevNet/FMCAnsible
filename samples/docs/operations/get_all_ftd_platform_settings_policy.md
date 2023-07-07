# getAllFTDPlatformSettingsPolicy

The getAllFTDPlatformSettingsPolicy operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/ftdplatformsettingspolicies](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/ftdplatformsettingspolicies.md) path.&nbsp;
## Description
**Retrieves the FTDPlatformSettings Policy with the associated ID. If no ID is specified, retrieves a list of all FTDPlatformSettings Policies.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| filter | False | string <td colspan=3> Filter criteria can be specified using the format <code>name:policy_name</code><br/><br/><code>policy_name</code> -- Name of the FTDPlatformSettings Policy to be queried. |
| offset | False | integer <td colspan=3> Index of first item to return. |
| limit | False | integer <td colspan=3> Number of items to return. |
| expanded | False | boolean <td colspan=3> If set to true, the GET response displays a list of objects with additional attributes. |

## Example
```yaml
- name: Execute 'getAllFTDPlatformSettingsPolicy' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getAllFTDPlatformSettingsPolicy"
    path_params:
        domainUUID: "{{ domain_uuid }}"
    query_params:
        filter: "{{ filter }}"
        offset: "{{ offset }}"
        limit: "{{ limit }}"
        expanded: "{{ expanded }}"

```