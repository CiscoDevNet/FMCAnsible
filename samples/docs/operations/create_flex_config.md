# createFlexConfig

The createFlexConfig operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/flexconfigpolicies](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/flexconfigpolicies.md) path.&nbsp;
## Description
**Retrieves the FlexConfig Policy with the associated ID. If no ID is specified, retrieves a list of all FlexConfig Policies. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createFlexConfig' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createFlexConfig"
    path_params:
        domainUUID: "{{ domain_uuid }}"

```