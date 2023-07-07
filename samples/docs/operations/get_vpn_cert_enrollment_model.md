# getVpnCertEnrollmentModel

The getVpnCertEnrollmentModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/certenrollments/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/certenrollments/{object_id}.md) path.&nbsp;
## Description
**&#91;DEV ERROR: Missing description&#93;**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> [DEV ERROR: Missing description] |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'getVpnCertEnrollmentModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getVpnCertEnrollmentModel"
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```