# createSIURLList

The createSIURLList operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/siurllists](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/siurllists.md) path.&nbsp;
## Description
**Retrieves, creates, deletes or modifies the Security Intelligence URL List object associated with the specified ID. If no ID is specified, retrieves list of all Security Intelligence URL List objects. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| name | List_1 |
| fileName | urls.txt |
| type | SIURLList |
| listType | 4 |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createSIURLList' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createSIURLList"
    data:
        name: List_1
        fileName: urls.txt
        type: SIURLList
        listType: 4
    path_params:
        domainUUID: "{{ domain_uuid }}"

```