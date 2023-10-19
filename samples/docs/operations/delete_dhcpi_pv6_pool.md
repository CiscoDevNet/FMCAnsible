# deleteDHCPIPv6Pool

The deleteDHCPIPv6Pool operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/dhcpipv6pools/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/dhcpipv6pools/{object_id}.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the DHCP IPv6 pool object associated with the specified ID. If no ID is specified, retrieves list of all DHCP IPv6 Pool objects _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Unique identifier of a DHCP IPv6 pool object. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'deleteDHCPIPv6Pool' operation
  cisco.fmcansible.fmc_configuration:
    operation: "deleteDHCPIPv6Pool"
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```