# createFTDLoopbackInterface

The createFTDLoopbackInterface operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/loopbackinterfaces](/paths//api/fmc_config/v1/domain/{domain_uuid}/devices/devicerecords/{container_uuid}/loopbackinterfaces.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the loopback interface associated with the specified NGFW device ID and/or interface ID. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| type | LoopbackInterface |
| loopbackId | 5 |
| enabled | True |
| ifname | loopback-5 |
| ipv4 | {'static': {'address': '169.254.100.1', 'netmask': '255.255.255.252'}} |
| ipv6 | {'addresses': [{'address': 'ee::11', 'prefix': '64'}]} |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createFTDLoopbackInterface' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createFTDLoopbackInterface"
    data:
        type: LoopbackInterface
        loopbackId: 5
        enabled: True
        ifname: loopback-5
        ipv4: {'static': {'address': '169.254.100.1', 'netmask': '255.255.255.252'}}
        ipv6: {'addresses': [{'address': 'ee::11', 'prefix': '64'}]}
    path_params:
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```