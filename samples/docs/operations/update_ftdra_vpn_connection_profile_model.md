# updateFTDRAVpnConnectionProfileModel

The updateFTDRAVpnConnectionProfileModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/ravpns/{containerUUID}/connectionprofiles/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/ravpns/{container_uuid}/connectionprofiles/{object_id}.md) path.&nbsp;
## Description
**Retrieves Connection Profile data inside a VPN RA Topology. If no ID is specified for a GET, retrieves list containing a single Connection Profile entry of the topology. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| id | <UUID> |
| name | <Name> |
| type | RaVpnConnectionProfile |
| groupAlias | [{'aliasName': '<Name>', 'enabled': True}] |
| groupPolicy | {'name': '<Name>', 'id': '<UUID>', 'type': 'GroupPolicy'} |
| ipv4AddressPool | [{'name': '<Name>', 'id': '<UUID>', 'type': 'IPv4AddressPool'}] |
| primaryAuthenticationServer | {'name': '<Name>', 'id': '<UUID>', 'type': 'Realm'} |
| dhcpServersForAddressAssignment | [{'name': '<Name>', 'id': '<UUID>', 'type': 'NetworkObject'}] |
| allowConnectionOnlyIfAuthorized | False |
| stripRealmFromUsername | False |
| stripGroupFromUsername | False |
| enablePasswordManagement | False |
| useLocalAsPrimaryAuthServer | False |
| enablePrimaryAuthFallbackToLocal | False |
| useLocalAsSecondaryAuthServer | False |
| enableSecondaryAuthFallbackToLocal | False |
| enableSecondaryAuthentication | False |
| authenticationMethod | AAA_ONLY |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier for Connection Profile in a RA VPN topology. |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'updateFTDRAVpnConnectionProfileModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateFTDRAVpnConnectionProfileModel"
    data:
        id: <UUID>
        name: <Name>
        type: RaVpnConnectionProfile
        groupAlias: [{'aliasName': '<Name>', 'enabled': True}]
        groupPolicy: {'name': '<Name>', 'id': '<UUID>', 'type': 'GroupPolicy'}
        ipv4AddressPool: [{'name': '<Name>', 'id': '<UUID>', 'type': 'IPv4AddressPool'}]
        primaryAuthenticationServer: {'name': '<Name>', 'id': '<UUID>', 'type': 'Realm'}
        dhcpServersForAddressAssignment: [{'name': '<Name>', 'id': '<UUID>', 'type': 'NetworkObject'}]
        allowConnectionOnlyIfAuthorized: False
        stripRealmFromUsername: False
        stripGroupFromUsername: False
        enablePasswordManagement: False
        useLocalAsPrimaryAuthServer: False
        enablePrimaryAuthFallbackToLocal: False
        useLocalAsSecondaryAuthServer: False
        enableSecondaryAuthFallbackToLocal: False
        enableSecondaryAuthentication: False
        authenticationMethod: AAA_ONLY
    path_params:
        objectId: "{{ object_id }}"
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```