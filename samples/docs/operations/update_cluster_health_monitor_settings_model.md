# updateClusterHealthMonitorSettingsModel

The updateClusterHealthMonitorSettingsModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/deviceclusters/ftddevicecluster/{containerUUID}/clusterhealthmonitorsettings/{clusterUuid}](/paths//api/fmc_config/v1/domain/{domain_uuid}/deviceclusters/ftddevicecluster/{container_uuid}/clusterhealthmonitorsettings/{cluster_uuid}.md) path.&nbsp;
## Description
**Represents health check monitor settings of Firewall Threat Defense Cluster. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| clusterUuid | True | string <td colspan=3> Identifier of a Firewall Threat Defense Cluster. |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| partialUpdate | False | boolean <td colspan=3> This is a query parameter. Default value is <code>false</code>. This field specifies whether to change the entire object or only certain attributes of it. When its value is <code>false</code> the whole object will change, and if the value is <code>true</code> then only the attributes that are specified will change. |

## Example
```yaml
- name: Execute 'updateClusterHealthMonitorSettingsModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateClusterHealthMonitorSettingsModel"
    path_params:
        clusterUuid: "{{ cluster_uuid }}"
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"
    query_params:
        partialUpdate: "{{ partial_update }}"

```