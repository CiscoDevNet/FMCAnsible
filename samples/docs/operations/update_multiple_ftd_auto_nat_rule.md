# updateMultipleFTDAutoNatRule

The updateMultipleFTDAutoNatRule operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/ftdnatpolicies/{containerUUID}/autonatrules](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/ftdnatpolicies/{container_uuid}/autonatrules.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the Auto NAT rule associated with the specified ID. Also, retrieves list of all Auto NAT rules. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| originalNetwork | {'type': 'Network', 'id': 'Network object uuid'} |
| translatedNetwork | {'type': 'Network', 'id': 'Network object uuid'} |
| id | autoNatRuleUuid |
| type | FTDAutoNatRule |
| natType | STATIC |
| interfaceIpv6 | False |
| fallThrough | False |
| dns | False |
| routeLookup | False |
| noProxyArp | False |
| netToNet | False |
| sourceInterface | {'id': 'security zone uuid', 'type': 'SecurityZone'} |
| destinationInterface | {'id': 'security zone uuid', 'type': 'SecurityZone'} |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| bulk | False | boolean <td colspan=3> Enables bulk actions for Auto NAT rules. |
| partialUpdate | False | boolean <td colspan=3> This field specifies whether to change the entire object or only certain attributes of it. When its value is false the whole object will change, and if the value is true then only the attributes that are specified will change. The default value of this field is false. |

## Example
```yaml
- name: Execute 'updateMultipleFTDAutoNatRule' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateMultipleFTDAutoNatRule"
    data:
        originalNetwork: {'type': 'Network', 'id': 'Network object uuid'}
        translatedNetwork: {'type': 'Network', 'id': 'Network object uuid'}
        id: autoNatRuleUuid
        type: FTDAutoNatRule
        natType: STATIC
        interfaceIpv6: False
        fallThrough: False
        dns: False
        routeLookup: False
        noProxyArp: False
        netToNet: False
        sourceInterface: {'id': 'security zone uuid', 'type': 'SecurityZone'}
        destinationInterface: {'id': 'security zone uuid', 'type': 'SecurityZone'}
    path_params:
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"
    query_params:
        bulk: "{{ bulk }}"
        partialUpdate: "{{ partial_update }}"

```