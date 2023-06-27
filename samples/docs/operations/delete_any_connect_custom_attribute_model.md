# deleteAnyConnectCustomAttributeModel

The deleteAnyConnectCustomAttributeModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/anyconnectcustomattributes/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/anyconnectcustomattributes/{object_id}.md) path.&nbsp;
## Description
**Retrieves the AnyConnect Custom Attribute associated with the specified ID. If no ID is specified for a GET, retrieves list of all AnyConnect Custom Attribute objects. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier for AnyConnect Custom Attribute object. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'deleteAnyConnectCustomAttributeModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "deleteAnyConnectCustomAttributeModel"
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```