# deleteAnyConnectPackageModel

The deleteAnyConnectPackageModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/anyconnectpackages/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/anyconnectpackages/{object_id}.md) path.&nbsp;
## Description
**Retrieves, update, deletes or creates the AnyConnect Package associated with the specified ID. If no ID is specified for a GET, retrieves list of all AnyConnect Package objects. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier for AnyConnect Package object. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'deleteAnyConnectPackageModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "deleteAnyConnectPackageModel"
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```