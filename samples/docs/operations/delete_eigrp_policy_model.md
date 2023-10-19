# deleteEigrpPolicyModel

The deleteEigrpPolicyModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/eigrproutes/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/devices/devicerecords/{container_uuid}/routing/eigrproutes/{object_id}.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the EIGRP associated with the specified ID. Also, retrieves list of all EIGRP. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Unique identifier of a EIGRP. |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'deleteEigrpPolicyModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "deleteEigrpPolicyModel"
    path_params:
        objectId: "{{ object_id }}"
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```