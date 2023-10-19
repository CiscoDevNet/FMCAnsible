# updateGroupPolicyModel

The updateGroupPolicyModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/grouppolicies/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/grouppolicies/{object_id}.md) path.&nbsp;
## Description
**Defines  the group policies for VPN _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| enableSSLProtocol | True |
| enableIPsecIKEv2Protocol | True |
| generalSettings | {'splitTunnelSettings': {'ipv4SplitTunnelPolicy': 'TUNNEL_ALL', 'ipv6SplitTunnelPolicy': 'TUNNEL_ALL', 'splitDNSRequestPolicy': 'USE_SPLIT_TUNNEL_SETTING'}, 'addressAssignment': {'ipv4LocalAddressPool': [{'name': 'ipv4_pool_1', 'id': '00505681-162B-0ed3-0000-476741369859', 'type': 'IPv4AddressPool'}], 'dhcpScope': {'name': 'obj', 'id': '00505681-162B-0ed3-0000-536870912003', 'type': 'Network'}}, 'primaryDNSServer': {'name': 'host_1', 'id': '00505681-162B-0ed3-0000-536870912021', 'type': 'Host'}, 'secondaryDNSServer': {'name': 'host_2', 'id': '00505681-162B-0ed3-0000-536870912039', 'type': 'Host'}, 'primaryWINSServer': {'name': 'host_3', 'id': '00505681-162B-0ed3-0000-536870912057', 'type': 'Host'}, 'secondaryWINSServer': {'name': 'host_4', 'id': '00505681-162B-0ed3-0000-536870912075', 'type': 'Host'}, 'banner': 'banner'} |
| anyConnectSettings | {'sslSettings': {'mtuSize': 1406, 'ignoreDFBit': False, 'sslCompression': 'DISABLED', 'dtlsCompression': 'DISABLED'}, 'connectionSettings': {'rekeyMethod': 'NEW_TUNNEL', 'enableGatewayDPD': True, 'enableClientDPD': True, 'enableSSLRekey': False, 'enableKeepAliveMessages': True, 'keepAliveMessageInterval': 20, 'gatewayDPDInterval': 30, 'clientDPDInterval': 30, 'bypassUnsupportProtocol': False, 'rekeyInterval': 4}, 'customAttributes': [{'anyConnectAttribute': 'PER_APP_VPN', 'customAttributeObject': {'name': 'custom_attr_2', 'id': '00505681-162B-0ed3-0000-966367641621', 'type': 'AnyConnectCustomAttribute'}}]} |
| advancedSettings | {'sessionSettings': {'vpnIdleTimeout': 30, 'maxConnectionTimeAlertInterval': 1, 'maxConnectionTimeout': -1, 'simultaneousLoginPerUser': 3, 'vpnIdleTimeoutAlertInterval': 1}} |
| type | GroupPolicy |
| name | rest_1 |
| description | description |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Unique identifier of the Group policy. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'updateGroupPolicyModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateGroupPolicyModel"
    data:
        enableSSLProtocol: True
        enableIPsecIKEv2Protocol: True
        generalSettings: {'splitTunnelSettings': {'ipv4SplitTunnelPolicy': 'TUNNEL_ALL', 'ipv6SplitTunnelPolicy': 'TUNNEL_ALL', 'splitDNSRequestPolicy': 'USE_SPLIT_TUNNEL_SETTING'}, 'addressAssignment': {'ipv4LocalAddressPool': [{'name': 'ipv4_pool_1', 'id': '00505681-162B-0ed3-0000-476741369859', 'type': 'IPv4AddressPool'}], 'dhcpScope': {'name': 'obj', 'id': '00505681-162B-0ed3-0000-536870912003', 'type': 'Network'}}, 'primaryDNSServer': {'name': 'host_1', 'id': '00505681-162B-0ed3-0000-536870912021', 'type': 'Host'}, 'secondaryDNSServer': {'name': 'host_2', 'id': '00505681-162B-0ed3-0000-536870912039', 'type': 'Host'}, 'primaryWINSServer': {'name': 'host_3', 'id': '00505681-162B-0ed3-0000-536870912057', 'type': 'Host'}, 'secondaryWINSServer': {'name': 'host_4', 'id': '00505681-162B-0ed3-0000-536870912075', 'type': 'Host'}, 'banner': 'banner'}
        anyConnectSettings: {'sslSettings': {'mtuSize': 1406, 'ignoreDFBit': False, 'sslCompression': 'DISABLED', 'dtlsCompression': 'DISABLED'}, 'connectionSettings': {'rekeyMethod': 'NEW_TUNNEL', 'enableGatewayDPD': True, 'enableClientDPD': True, 'enableSSLRekey': False, 'enableKeepAliveMessages': True, 'keepAliveMessageInterval': 20, 'gatewayDPDInterval': 30, 'clientDPDInterval': 30, 'bypassUnsupportProtocol': False, 'rekeyInterval': 4}, 'customAttributes': [{'anyConnectAttribute': 'PER_APP_VPN', 'customAttributeObject': {'name': 'custom_attr_2', 'id': '00505681-162B-0ed3-0000-966367641621', 'type': 'AnyConnectCustomAttribute'}}]}
        advancedSettings: {'sessionSettings': {'vpnIdleTimeout': 30, 'maxConnectionTimeAlertInterval': 1, 'maxConnectionTimeout': -1, 'simultaneousLoginPerUser': 3, 'vpnIdleTimeoutAlertInterval': 1}}
        type: GroupPolicy
        name: rest_1
        description: description
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```