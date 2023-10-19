# deleteUpgradePackage

The deleteUpgradePackage operation handles configuration related to [/api/fmc_platform/v1/updates/upgradepackages/{objectId}](/paths//api/fmc_platform/v1/updates/upgradepackages/{object_id}.md) path.&nbsp;
## Description
**GET: Retrieves the upgrade packages associated with the specified ID.If no ID is specified, retrieves list of all upgrade packages.DELETE: Deletes the upgrade package associated with the specified ID. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Unique identifier of the object. |

## Example
```yaml
- name: Execute 'deleteUpgradePackage' operation
  cisco.fmcansible.fmc_configuration:
    operation: "deleteUpgradePackage"
    path_params:
        objectId: "{{ object_id }}"

```