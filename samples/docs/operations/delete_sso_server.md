# deleteSSOServer

The deleteSSOServer operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/ssoservers/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/ssoservers/{object_id}.md) path.&nbsp;
## Description
**Retrieves the SSO Server Policy Object associated with the specified ID. If no ID is specified, retrieves list of all SSO Server Policy Objects. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Unique identifier of the SSO Server Policy Object. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'deleteSSOServer' operation
  cisco.fmcansible.fmc_configuration:
    operation: "deleteSSOServer"
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```