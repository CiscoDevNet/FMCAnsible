# createCSDACStatus

The createCSDACStatus operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/health/csdac](/paths//api/fmc_config/v1/domain/{domain_uuid}/health/csdac.md) path.&nbsp;
## Description
**Retrieves or updates the Cisco Secure Dynamic Attributes Connector status for the device. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createCSDACStatus' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createCSDACStatus"
    path_params:
        domainUUID: "{{ domain_uuid }}"

```