# createTestUmbrellaConnection

The createTestUmbrellaConnection operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/integration/operational/testumbrellaconnections](/paths//api/fmc_config/v1/domain/{domain_uuid}/integration/operational/testumbrellaconnections.md) path.&nbsp;
## Description
**Tests connection to the umbrella cloud. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createTestUmbrellaConnection' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createTestUmbrellaConnection"
    path_params:
        domainUUID: "{{ domain_uuid }}"

```