# updateFTDLoopbackInterface

The updateFTDLoopbackInterface operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/loopbackinterfaces/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/devices/devicerecords/{container_uuid}/loopbackinterfaces/{object_id}.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the loopback interface associated with the specified NGFW device ID and/or interface ID. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| type | LoopbackInterface |
| name | Loopback5 |
| loopbackId | 5 |
| enabled | True |
| ifname | loopback-5 |
| ipv4 | {'static': {'address': '2.2.2.2', 'netmask': '255.255.255.0'}} |
| id | 00000000-0000-0ed3-0000-206158430258 |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Unique identifier of a NGFW loopback interface. |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'updateFTDLoopbackInterface' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateFTDLoopbackInterface"
    data:
        type: LoopbackInterface
        name: Loopback5
        loopbackId: 5
        enabled: True
        ifname: loopback-5
        ipv4: {'static': {'address': '2.2.2.2', 'netmask': '255.255.255.0'}}
        id: 00000000-0000-0ed3-0000-206158430258
    path_params:
        objectId: "{{ object_id }}"
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```