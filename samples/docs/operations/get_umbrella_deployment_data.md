# getUmbrellaDeploymentData

The getUmbrellaDeploymentData operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/integration/umbrella/tunneldeployments/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/integration/umbrella/tunneldeployments/{object_id}.md) path.&nbsp;
## Description
**Retrieves Tunnel deployment data on Umbrella.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Unique identifier of Umbrella Topology to be deployed. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'getUmbrellaDeploymentData' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getUmbrellaDeploymentData"
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```