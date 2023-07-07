# updateInternalCertificate

The updateInternalCertificate operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/internalcertificates/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/internalcertificates/{object_id}.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the Internal Certificate associated with the specified ID. If no ID is specified, retrieves list of all Internal Certificates. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| name | postman_cert_5_modified |
| id | 2d615d16-96b5-11ec-a9ec-6765f7cbab59 |
| version | 220bf15e-96bc-11ec-a6e0-6465f7cbab59 |
| type | InternalCertificate |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Unique identifier of an Internal Certificate. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'updateInternalCertificate' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateInternalCertificate"
    data:
        name: postman_cert_5_modified
        id: 2d615d16-96b5-11ec-a9ec-6765f7cbab59
        version: 220bf15e-96bc-11ec-a6e0-6465f7cbab59
        type: InternalCertificate
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```