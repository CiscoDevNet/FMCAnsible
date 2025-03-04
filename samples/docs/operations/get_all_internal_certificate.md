# getAllInternalCertificate

The getAllInternalCertificate operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/internalcertificates](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/internalcertificates.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the Internal Certificate associated with the specified ID. If no ID is specified, retrieves list of all Internal Certificates.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| filter | False | string <td colspan=3> Filter by name of certificate is supported. |
| offset | False | integer <td colspan=3> Index of first item to return. |
| limit | False | integer <td colspan=3> Number of items to return. |
| expanded | False | boolean <td colspan=3> If set to true, the GET response displays a list of objects with additional attributes. |

## Example
```yaml
- name: Execute 'getAllInternalCertificate' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getAllInternalCertificate"
    path_params:
        domainUUID: "{{ domain_uuid }}"
    query_params:
        filter: "{{ filter }}"
        offset: "{{ offset }}"
        limit: "{{ limit }}"
        expanded: "{{ expanded }}"

```