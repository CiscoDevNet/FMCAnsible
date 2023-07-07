# createMultipleSSOServer

The createMultipleSSOServer operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/ssoservers](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/ssoservers.md) path.&nbsp;
## Description
**Retrieves the SSO Server Policy Object associated with the specified ID. If no ID is specified, retrieves list of all SSO Server Policy Objects. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| bulk | False | boolean <td colspan=3> Enables bulk create for SSO Server Policy Objects. |

## Example
```yaml
- name: Execute 'createMultipleSSOServer' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createMultipleSSOServer"
    path_params:
        domainUUID: "{{ domain_uuid }}"
    query_params:
        bulk: "{{ bulk }}"

```