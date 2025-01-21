# createIPv4AddressPool

The createIPv4AddressPool operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/ipv4addresspools](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/ipv4addresspools.md) path.&nbsp;
## Description
**Retrieves the IPv4 Address Pool object associated with the specified ID. If no ID is specified for a GET, retrieves list of all IPv4 Address Pool objects. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| type | IPv4AddressPool |
| addressType | SUPERNET |
| supernetAddress | 10.10.0.0 |
| supernetPrefix | 16 |
| subnetPrefix | 24 |
| rangeStart | 1 |
| numberOfAddresses | 50 |
| overridable | True |
| description |   |
| name | adpoolNW_51 |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createIPv4AddressPool' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createIPv4AddressPool"
    data:
        type: IPv4AddressPool
        addressType: SUPERNET
        supernetAddress: 10.10.0.0
        supernetPrefix: 16
        subnetPrefix: 24
        rangeStart: 1
        numberOfAddresses: 50
        overridable: True
        description:  
        name: adpoolNW_51
    path_params:
        domainUUID: "{{ domain_uuid }}"

```