# createVpnCertEnrollmentModel

The createVpnCertEnrollmentModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/certenrollments](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/certenrollments.md) path.&nbsp;
## Description
**&#91;DEV ERROR: Missing description&#93; _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createVpnCertEnrollmentModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createVpnCertEnrollmentModel"
    path_params:
        domainUUID: "{{ domain_uuid }}"

```