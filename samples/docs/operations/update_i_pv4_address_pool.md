# updateIPv4AddressPool

The updateIPv4AddressPool operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/ipv4addresspools/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/ipv4addresspools/{object_id}.md) path.&nbsp;
## Description
**Retrieves the IPv4 Address Pool object associated with the specified ID. If no ID is specified for a GET, retrieves list of all IPv4 Address Pool objects. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| mask | 255.255.255.192 |
| type | IPv4AddressPool |
| ipAddressRange | 10.10.19.10-10.10.19.20 |
| id | 00505686-154A-0ed3-0000-008589935142 |
| overridable | True |
| description |   |
| name | adpool |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Unique identifier of the object. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'updateIPv4AddressPool' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateIPv4AddressPool"
    data:
        mask: 255.255.255.192
        type: IPv4AddressPool
        ipAddressRange: 10.10.19.10-10.10.19.20
        id: 00505686-154A-0ed3-0000-008589935142
        overridable: True
        description:  
        name: adpool
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```