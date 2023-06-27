# getUmbrellaConnection

The getUmbrellaConnection operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/integration/umbrellaconnections/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/integration/umbrellaconnections/{object_id}.md) path.&nbsp;
## Description
**Retrieves Umbrella connection configuration.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Unique identifier of an Umbrella connection building block |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'getUmbrellaConnection' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getUmbrellaConnection"
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```