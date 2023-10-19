# getAllDHCPIPv6Pool

The getAllDHCPIPv6Pool operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/dhcpipv6pools](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/dhcpipv6pools.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the DHCP IPv6 pool object associated with the specified ID. If no ID is specified, retrieves list of all DHCP IPv6 Pool objects**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| offset | False | integer <td colspan=3> Index of first item to return. |
| limit | False | integer <td colspan=3> Number of items to return. |
| expanded | False | boolean <td colspan=3> If set to true, the GET response displays a list of objects with additional attributes. |

## Example
```yaml
- name: Execute 'getAllDHCPIPv6Pool' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getAllDHCPIPv6Pool"
    path_params:
        domainUUID: "{{ domain_uuid }}"
    query_params:
        offset: "{{ offset }}"
        limit: "{{ limit }}"
        expanded: "{{ expanded }}"

```