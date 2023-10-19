# getClusterHealthMonitorSettingsModel

The getClusterHealthMonitorSettingsModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/deviceclusters/ftddevicecluster/{containerUUID}/clusterhealthmonitorsettings/{clusterUuid}](/paths//api/fmc_config/v1/domain/{domain_uuid}/deviceclusters/ftddevicecluster/{container_uuid}/clusterhealthmonitorsettings/{cluster_uuid}.md) path.&nbsp;
## Description
**Represents health check monitor settings of Firewall Threat Defense Cluster.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| clusterUuid | True | string <td colspan=3> Identifier of a Firewall Threat Defense Cluster. |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'getClusterHealthMonitorSettingsModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getClusterHealthMonitorSettingsModel"
    path_params:
        clusterUuid: "{{ cluster_uuid }}"
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```