# getFTDPlatformSettingsPolicy

The getFTDPlatformSettingsPolicy operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/ftdplatformsettingspolicies/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/ftdplatformsettingspolicies/{object_id}.md) path.&nbsp;
## Description
**Retrieves the FTDPlatformSettings Policy with the associated ID. If no ID is specified, retrieves a list of all FTDPlatformSettings Policies.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Unique identifier of a FTDPlatformSettings policy. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'getFTDPlatformSettingsPolicy' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getFTDPlatformSettingsPolicy"
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```