# getAllUpgradePackage

The getAllUpgradePackage operation handles configuration related to [/api/fmc_platform/v1/updates/upgradepackages](/paths//api/fmc_platform/v1/updates/upgradepackages.md) path.&nbsp;
## Description
**GET: Retrieves the upgrade packages associated with the specified ID.If no ID is specified, retrieves list of all upgrade packages.DELETE: Deletes the upgrade package associated with the specified ID.**

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| offset | False | integer <td colspan=3> Index of first item to return. |
| limit | False | integer <td colspan=3> Number of items to return. |
| expanded | False | boolean <td colspan=3> If set to true, the GET response displays a list of objects with additional attributes. |

## Example
```yaml
- name: Execute 'getAllUpgradePackage' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getAllUpgradePackage"
    query_params:
        offset: "{{ offset }}"
        limit: "{{ limit }}"
        expanded: "{{ expanded }}"

```