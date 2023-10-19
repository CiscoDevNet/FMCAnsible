# updateSIURLList

The updateSIURLList operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/siurllists/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/siurllists/{object_id}.md) path.&nbsp;
## Description
**Retrieves, creates, deletes or modifies the Security Intelligence URL List object associated with the specified ID. If no ID is specified, retrieves list of all Security Intelligence URL List objects. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| name | List_1_Edited |
| fileName | urls.txt |
| type | SIURLList |
| listType | 4 |
| id | fc79ce12-069a-11ed-87bb-780a89d43a90 |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier of Security Intelligence URL List object. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'updateSIURLList' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateSIURLList"
    data:
        name: List_1_Edited
        fileName: urls.txt
        type: SIURLList
        listType: 4
        id: fc79ce12-069a-11ed-87bb-780a89d43a90
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```