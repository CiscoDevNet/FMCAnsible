# getAllBFDPolicyModel

The getAllBFDPolicyModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/bfdpolicies](/paths//api/fmc_config/v1/domain/{domain_uuid}/devices/devicerecords/{container_uuid}/routing/bfdpolicies.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the BFD Policy associated with the specified ID. If no ID is specified for a GET, retrieves list of all BFD Policies.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| filter | False | string <td colspan=3> To filter BFD policies based on hop type, use <code>hopType:{hopType}</code>. Supported hop types are Single-Hop and Multi-Hop.<br/><br/>To filter BFD policies objects based on IP type, use <code>ipType:{ipType}</code>. Supported ip types are v4 and v6. |
| offset | False | integer <td colspan=3> Index of first item to return. |
| limit | False | integer <td colspan=3> Number of items to return. |
| expanded | False | boolean <td colspan=3> If set to true, the GET response displays a list of objects with additional attributes. |

## Example
```yaml
- name: Execute 'getAllBFDPolicyModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getAllBFDPolicyModel"
    path_params:
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"
    query_params:
        filter: "{{ filter }}"
        offset: "{{ offset }}"
        limit: "{{ limit }}"
        expanded: "{{ expanded }}"

```