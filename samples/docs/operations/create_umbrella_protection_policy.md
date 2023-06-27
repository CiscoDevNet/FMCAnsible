# createUmbrellaProtectionPolicy

The createUmbrellaProtectionPolicy operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/operational/umbrellaprotectionpolicies](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/operational/umbrellaprotectionpolicies.md) path.&nbsp;
## Description
**Retrieves Umbrella protection policy configuration from umbrella cloud. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createUmbrellaProtectionPolicy' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createUmbrellaProtectionPolicy"
    path_params:
        domainUUID: "{{ domain_uuid }}"

```