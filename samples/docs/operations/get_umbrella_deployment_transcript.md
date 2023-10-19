# getUmbrellaDeploymentTranscript

The getUmbrellaDeploymentTranscript operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/integration/umbrella/tunneldeployments/{containerUUID}/transcripts/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/integration/umbrella/tunneldeployments/{container_uuid}/transcripts/{object_id}.md) path.&nbsp;
## Description
**Retrieves Transcript for Umbrella deployment for a given device and topology.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Unique identifier of Device to fetch corresponding Umbrella Transcript |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'getUmbrellaDeploymentTranscript' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getUmbrellaDeploymentTranscript"
    path_params:
        objectId: "{{ object_id }}"
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```