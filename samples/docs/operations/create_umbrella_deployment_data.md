# createUmbrellaDeploymentData

The createUmbrellaDeploymentData operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/integration/umbrella/tunneldeployments](/paths//api/fmc_config/v1/domain/{domain_uuid}/integration/umbrella/tunneldeployments.md) path.&nbsp;
## Description
**Retrieves Tunnel deployment data on Umbrella. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createUmbrellaDeploymentData' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createUmbrellaDeploymentData"
    path_params:
        domainUUID: "{{ domain_uuid }}"

```