# getRestFTDClusterDeviceContainer

The getRestFTDClusterDeviceContainer operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/deviceclusters/ftddevicecluster/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/deviceclusters/ftddevicecluster/{object_id}.md) path.&nbsp;
## Description
**Retrieves or modifies the Firewall Threat Defense Cluster record associated with the specified ID. If no ID is specified for a GET, retrieves list of all Firewall Threat Defense Clusters.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier of a Firewall Threat Defense Cluster. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| liveStatus | False | string <td colspan=3> Boolean to specify if live status of cluster nodes is required. |

## Example
```yaml
- name: Execute 'getRestFTDClusterDeviceContainer' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getRestFTDClusterDeviceContainer"
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"
    query_params:
        liveStatus: "{{ live_status }}"

```