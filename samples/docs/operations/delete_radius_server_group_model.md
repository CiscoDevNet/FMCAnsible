# deleteRadiusServerGroupModel

The deleteRadiusServerGroupModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/radiusservergroups/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/radiusservergroups/{object_id}.md) path.&nbsp;
## Description
**Retrieves the Radius Server Group associated with the specified ID. If no ID is specified for a GET, retrieves list of all Radius Server Group objects. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier for Radius Server Group object. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'deleteRadiusServerGroupModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "deleteRadiusServerGroupModel"
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```