# updateVrfEigrpPolicyModel

The updateVrfEigrpPolicyModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{virtualrouterUUID}/eigrproutes/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/devices/devicerecords/{container_uuid}/routing/virtualrouters/{virtualrouter_uuid}/eigrproutes/{object_id}.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the EIGRP associated for a specified virtual router with the specified ID. Also, retrieves list of all EIGRP. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| asNumber | 1 |
| type | EigrpRoute |
| id | eigrpUuid |
| redistributeProtocols | [{'protocol': 'RIP', 'routeMap': {'name': 'routeMapObject', 'id': '00505686-13CC-0ed3-0000-042949673437', 'type': 'RouteMapObject'}, 'matchExternal1': False, 'matchExternal2': False, 'matchInternal': False, 'matchNssaExternal1': False, 'matchNssaExternal2': False, 'routeMetric': {'bandwidth': 1, 'delay': 1, 'reliability': 1, 'effectiveBandwidth': 1, 'pathMTU': 1}}] |
| summaryAddressList | [{'deviceInterface': {'ifname': 'GigEth1', 'type': 'PhysicalInterface', 'id': 'interface_uuid', 'name': 'GigabitEthernet0/1'}, 'summaryAddress': {'name': 'any-ipv4', 'id': 'cb7116e8-66a6-480b-8f9b-295191a0940a', 'type': 'Network'}, 'adminDistance': 1}] |
| eigrpInterfaces | [{'deviceInterface': {'ifname': 'GigEth1', 'type': 'PhysicalInterface', 'id': 'interface_uuid', 'name': 'GigabitEthernet0/1'}, 'eigrpProtocolConfiguration': {'authentication': {'password': '1234', 'keyId': 2, 'pwdEncryption': 'ENCRYPTED', 'md5auth': True}, 'splitHorizon': False, 'timers': {'delay': 1, 'helloInterval': 1, 'holdTime': 1}}}] |
| basicConfiguration | {'networks': [{'name': 'any-ipv4', 'id': 'cb7116e8-66a6-480b-8f9b-295191a0940a', 'type': 'Network'}], 'autoSummary': False, 'passiveInterfaces': {'selectedInterfaces': [{'ifname': 'GigEth1', 'type': 'PhysicalInterface', 'id': 'interface_uuid', 'name': 'GigabitEthernet0/1'}], 'allInterfaces': False}} |
| advancedConfiguration | {'routerId': '1.1.1.1', 'logNeighborChanges': True, 'enableLogNeighborWarnings': True, 'logNeighborWarningInterval': 1, 'defaultRouteDistributionIn': {'name': 'AcessListObject', 'id': '00505686-13CC-0ed3-0000-042949673419', 'type': 'ACL'}, 'defaultRouteDistributionOut': {'name': 'AcessListObject', 'id': '00505686-13CC-0ed3-0000-042949673419', 'type': 'ACL'}, 'routeMetric': {'bandwidth': 1, 'delay': 1, 'reliability': 1, 'effectiveBandwidth': 1, 'pathMTU': 1}, 'stub': {'receiveOnly': True}, 'administrativeDistance': {'internal': 1, 'external': 1}} |
| neighbors | [{'neighborInterface': {'ifname': 'GigEth1', 'type': 'PhysicalInterface', 'id': 'interface_uuid', 'name': 'GigabitEthernet0/1'}, 'neighborAddress': {'name': 'networkObject1', 'id': 'network_object_uuid', 'type': 'Network'}}] |
| distributionList | [{'deviceInterface': {'ifname': 'GigEth1', 'type': 'PhysicalInterface', 'id': 'interface_uuid', 'name': 'GigabitEthernet0/1'}, 'accessList': {'name': 'AcessListObject', 'id': '00505686-13CC-0ed3-0000-042949673419', 'type': 'ACL'}, 'filterDirection': 'INBOUND'}] |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Unique identifier of a EIGRP. |
| virtualrouterUUID | True | string <td colspan=3> Unique identifier of Virtual Router |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'updateVrfEigrpPolicyModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateVrfEigrpPolicyModel"
    data:
        asNumber: 1
        type: EigrpRoute
        id: eigrpUuid
        redistributeProtocols: [{'protocol': 'RIP', 'routeMap': {'name': 'routeMapObject', 'id': '00505686-13CC-0ed3-0000-042949673437', 'type': 'RouteMapObject'}, 'matchExternal1': False, 'matchExternal2': False, 'matchInternal': False, 'matchNssaExternal1': False, 'matchNssaExternal2': False, 'routeMetric': {'bandwidth': 1, 'delay': 1, 'reliability': 1, 'effectiveBandwidth': 1, 'pathMTU': 1}}]
        summaryAddressList: [{'deviceInterface': {'ifname': 'GigEth1', 'type': 'PhysicalInterface', 'id': 'interface_uuid', 'name': 'GigabitEthernet0/1'}, 'summaryAddress': {'name': 'any-ipv4', 'id': 'cb7116e8-66a6-480b-8f9b-295191a0940a', 'type': 'Network'}, 'adminDistance': 1}]
        eigrpInterfaces: [{'deviceInterface': {'ifname': 'GigEth1', 'type': 'PhysicalInterface', 'id': 'interface_uuid', 'name': 'GigabitEthernet0/1'}, 'eigrpProtocolConfiguration': {'authentication': {'password': '1234', 'keyId': 2, 'pwdEncryption': 'ENCRYPTED', 'md5auth': True}, 'splitHorizon': False, 'timers': {'delay': 1, 'helloInterval': 1, 'holdTime': 1}}}]
        basicConfiguration: {'networks': [{'name': 'any-ipv4', 'id': 'cb7116e8-66a6-480b-8f9b-295191a0940a', 'type': 'Network'}], 'autoSummary': False, 'passiveInterfaces': {'selectedInterfaces': [{'ifname': 'GigEth1', 'type': 'PhysicalInterface', 'id': 'interface_uuid', 'name': 'GigabitEthernet0/1'}], 'allInterfaces': False}}
        advancedConfiguration: {'routerId': '1.1.1.1', 'logNeighborChanges': True, 'enableLogNeighborWarnings': True, 'logNeighborWarningInterval': 1, 'defaultRouteDistributionIn': {'name': 'AcessListObject', 'id': '00505686-13CC-0ed3-0000-042949673419', 'type': 'ACL'}, 'defaultRouteDistributionOut': {'name': 'AcessListObject', 'id': '00505686-13CC-0ed3-0000-042949673419', 'type': 'ACL'}, 'routeMetric': {'bandwidth': 1, 'delay': 1, 'reliability': 1, 'effectiveBandwidth': 1, 'pathMTU': 1}, 'stub': {'receiveOnly': True}, 'administrativeDistance': {'internal': 1, 'external': 1}}
        neighbors: [{'neighborInterface': {'ifname': 'GigEth1', 'type': 'PhysicalInterface', 'id': 'interface_uuid', 'name': 'GigabitEthernet0/1'}, 'neighborAddress': {'name': 'networkObject1', 'id': 'network_object_uuid', 'type': 'Network'}}]
        distributionList: [{'deviceInterface': {'ifname': 'GigEth1', 'type': 'PhysicalInterface', 'id': 'interface_uuid', 'name': 'GigabitEthernet0/1'}, 'accessList': {'name': 'AcessListObject', 'id': '00505686-13CC-0ed3-0000-042949673419', 'type': 'ACL'}, 'filterDirection': 'INBOUND'}]
    path_params:
        objectId: "{{ object_id }}"
        virtualrouterUUID: "{{ virtualrouter_uuid }}"
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```