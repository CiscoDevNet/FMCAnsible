# getAllBFDTemplate

The getAllBFDTemplate operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/bfdtemplates](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/bfdtemplates.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the BFDTemplate object associated with the specified ID. If no ID is specified for a GET, retrieves list of all Bidirectional Forwarding Detection routing template objects.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| filter | False | string <td colspan=3> To filter BFD templates based on hop type, use <code>hopType:{hopType}</code>. Supported hop types are Single-Hop and Multi-Hop. |
| offset | False | integer <td colspan=3> Index of first item to return. |
| limit | False | integer <td colspan=3> Number of items to return. |
| expanded | False | boolean <td colspan=3> If set to true, the GET response displays a list of objects with additional attributes. |

## Example
```yaml
- name: Execute 'getAllBFDTemplate' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getAllBFDTemplate"
    path_params:
        domainUUID: "{{ domain_uuid }}"
    query_params:
        filter: "{{ filter }}"
        offset: "{{ offset }}"
        limit: "{{ limit }}"
        expanded: "{{ expanded }}"

```