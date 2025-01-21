# createFlexConfigMigration

The createFlexConfigMigration operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/flexconfigpolicies/{containerUUID}/migrate](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/flexconfigpolicies/{container_uuid}/migrate.md) path.&nbsp;
## Description
**Initiates the flexConfig migration for specified devices. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createFlexConfigMigration' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createFlexConfigMigration"
    path_params:
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```