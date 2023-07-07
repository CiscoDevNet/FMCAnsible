# updateFTDRAVpnLoadBalanceSetting

The updateFTDRAVpnLoadBalanceSetting operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/ravpns/{containerUUID}/loadbalancesettings/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/ravpns/{container_uuid}/loadbalancesettings/{object_id}.md) path.&nbsp;
## Description
**Retrieves Load Balance Setting inside a VPN RA Topology. If no ID is specified for a GET, retrieves list containing a single Load Balance Setting entry of the topology. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| type | LoadBalanacing |
| redirectSettings | {'redirectUsingFqdn': False, 'ikev2RedirectPhase': 'DURING_SA_AUTHENTICATION'} |
| groupSettings | {'ipsecEncryption': {'encryptionKey': 'test', 'enable': True}, 'groupIPv4Address': '3.3.3.7', 'communicationInterface': {'name': 'sz_2', 'id': 'e121527c-ba53-11ec-a727-947db73fdfc8', 'type': 'SecurityZone'}, 'communicationUdpPort': 9023} |
| enableVpnLoadBalancing | True |
| participatingDevices | [{'priority': 6, 'device': {'name': '10.10.0.61', 'id': '5158c54a-b93a-11ec-9975-c81e12af82f6'}}] |
| name | F1RALoadBalancePolicy |
| id | 00505681-66E4-0ed3-0000-012884902090 |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier for Load Balance Setting in a RA VPN topology. |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'updateFTDRAVpnLoadBalanceSetting' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateFTDRAVpnLoadBalanceSetting"
    data:
        type: LoadBalanacing
        redirectSettings: {'redirectUsingFqdn': False, 'ikev2RedirectPhase': 'DURING_SA_AUTHENTICATION'}
        groupSettings: {'ipsecEncryption': {'encryptionKey': 'test', 'enable': True}, 'groupIPv4Address': '3.3.3.7', 'communicationInterface': {'name': 'sz_2', 'id': 'e121527c-ba53-11ec-a727-947db73fdfc8', 'type': 'SecurityZone'}, 'communicationUdpPort': 9023}
        enableVpnLoadBalancing: True
        participatingDevices: [{'priority': 6, 'device': {'name': '10.10.0.61', 'id': '5158c54a-b93a-11ec-9975-c81e12af82f6'}}]
        name: F1RALoadBalancePolicy
        id: 00505681-66E4-0ed3-0000-012884902090
    path_params:
        objectId: "{{ object_id }}"
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```