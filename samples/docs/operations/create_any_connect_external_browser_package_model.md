# createAnyConnectExternalBrowserPackageModel

The createAnyConnectExternalBrowserPackageModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/anyconnectexternalbrowserpackages](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/anyconnectexternalbrowserpackages.md) path.&nbsp;
## Description
**Retrieves, update, deletes or creates the AnyConnect External Browser Package associated with the specified ID. If no ID is specified for a GET, retrieves list of all AnyConnect External Browser Package objects. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createAnyConnectExternalBrowserPackageModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createAnyConnectExternalBrowserPackageModel"
    path_params:
        domainUUID: "{{ domain_uuid }}"

```