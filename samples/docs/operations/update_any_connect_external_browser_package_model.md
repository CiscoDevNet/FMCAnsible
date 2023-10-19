# updateAnyConnectExternalBrowserPackageModel

The updateAnyConnectExternalBrowserPackageModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/anyconnectexternalbrowserpackages/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/anyconnectexternalbrowserpackages/{object_id}.md) path.&nbsp;
## Description
**Retrieves, update, deletes or creates the AnyConnect External Browser Package associated with the specified ID. If no ID is specified for a GET, retrieves list of all AnyConnect External Browser Package objects. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| name | string |
| id | string |
| description | string |
| payloadFile | .pkg or .zip file |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier for AnyConnect External Browser Package object. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'updateAnyConnectExternalBrowserPackageModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateAnyConnectExternalBrowserPackageModel"
    data:
        name: string
        id: string
        description: string
        payloadFile: .pkg or .zip file
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```