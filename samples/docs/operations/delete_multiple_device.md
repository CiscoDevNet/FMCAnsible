# deleteMultipleDevice

The deleteMultipleDevice operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords](/paths//api/fmc_config/v1/domain/{domain_uuid}/devices/devicerecords.md) path.&nbsp;
## Description
**Retrieves or modifies the device record associated with the specified ID. Registers or unregisters a device. If no ID is specified for a GET, retrieves list of all device records. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| bulk | True | boolean <td colspan=3> Enables bulk registration or unregistration for devices. |
| filter | True | string <td colspan=3> Filter to retrieve or delete device records based upon filter parameters specified. <br/><br/>For bulk deletion, we need the filter="ids:" with <code>bulk=true</code> flag, Value is of format : <code>"ids:id1,id2,..."</code>.<br/><code>ids:id1,id2,...</code> is a comma-separated list of device uuids to be deleted.<br/><br/> For fetching device records, Filter criteria should be <code>name:{name};hostName:{hostName};serialNumber:{ABCXXXXX};containerType:{value};version:{x.x.x};clusterBootstrapSupported:{true|false};analyticsOnly:{true|false};includeOtherAssociatedPolicies:{true|false}</code><br/><br/><code>containerType</code> -- Allowed values are <code>{DeviceCluster|DeviceHAPair|DeviceStack}</code><br/><br/><code>clusterBootstrapSupported</code> -- Allowed values are <code>{true|false}</code><br/><br/><code>analyticsOnly</code> -- Allowed values are <code>{true|false}</code><br/><br/><code>includeOtherAssociatedPolicies</code> -- Allowed values are <code>{true|false}</code>. When set to <code>true</code>, will give following policies if assigned to device: [<code>RAVpn</code>,<code>FTDS2SVpn</code>,<code>PlatformSettingsPolicy</code>,<code>QosPolicy</code>,<code>NatPolicy</code>,<code>FlexConfigPolicy</code>] |

## Example
```yaml
- name: Execute 'deleteMultipleDevice' operation
  cisco.fmcansible.fmc_configuration:
    operation: "deleteMultipleDevice"
    path_params:
        domainUUID: "{{ domain_uuid }}"
    query_params:
        bulk: "{{ bulk }}"
        filter: "{{ filter }}"

```