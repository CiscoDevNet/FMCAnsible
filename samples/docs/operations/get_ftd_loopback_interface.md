# getFTDLoopbackInterface

The getFTDLoopbackInterface operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/loopbackinterfaces/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/devices/devicerecords/{container_uuid}/loopbackinterfaces/{object_id}.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the loopback interface associated with the specified NGFW device ID and/or interface ID.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Unique identifier of a NGFW loopback interface. |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'getFTDLoopbackInterface' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getFTDLoopbackInterface"
    path_params:
        objectId: "{{ object_id }}"
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```