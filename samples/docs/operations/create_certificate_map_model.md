# createCertificateMapModel

The createCertificateMapModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/certificatemaps](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/certificatemaps.md) path.&nbsp;
## Description
**Retrieves the Certificate Map associated with the specified ID. If no ID is specified for a GET, retrieves list of all Certificate Map objects. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createCertificateMapModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createCertificateMapModel"
    path_params:
        domainUUID: "{{ domain_uuid }}"

```