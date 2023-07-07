# getVrfEigrpPolicyModel

The getVrfEigrpPolicyModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{virtualrouterUUID}/eigrproutes/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/devices/devicerecords/{container_uuid}/routing/virtualrouters/{virtualrouter_uuid}/eigrproutes/{object_id}.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the EIGRP associated for a specified virtual router with the specified ID. Also, retrieves list of all EIGRP.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Unique identifier of a EIGRP. |
| virtualrouterUUID | True | string <td colspan=3> Unique identifier of Virtual Router |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'getVrfEigrpPolicyModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getVrfEigrpPolicyModel"
    path_params:
        objectId: "{{ object_id }}"
        virtualrouterUUID: "{{ virtualrouter_uuid }}"
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```