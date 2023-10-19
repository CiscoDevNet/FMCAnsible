# updateRadiusServerGroupModel

The updateRadiusServerGroupModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/radiusservergroups/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/radiusservergroups/{object_id}.md) path.&nbsp;
## Description
**Retrieves the Radius Server Group associated with the specified ID. If no ID is specified for a GET, retrieves list of all Radius Server Group objects. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| name | Radius-Server-1 |
| description | Radius-Server-1 desc |
| id | RadiusServerGroupUUID |
| type | RadiusServerGroup |
| retryInterval | 4 |
| dynamicAuthorizationPort | 1800 |
| interimAccountUpdateInterval | 110 |
| groupAccountingMode | MULTIPLE |
| realm | {'name': 'Realm', 'id': 'RealmUUID', 'type': 'Realm'} |
| enableAuthorizeOnly | True |
| enableInterimAccountUpdate | True |
| enableDynamicAuthorization | True |
| radiusServers | [{'timeout': 110, 'host': 'string', 'interface': {'name': 'String', 'id': 'InterfaceUUID', 'type': 'SecurityZone'}, 'serverSecretKey': '****', 'serverAuthenticationPort': 1812, 'serverAccountingPort': 1813, 'useRoutingToSelectInterface': True, 'redirectACL': {'name': 'string', 'id': 'ExtendedAccessListUUID', 'type': 'ExtendedAccessList'}}] |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier for Radius Server Group object. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'updateRadiusServerGroupModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateRadiusServerGroupModel"
    data:
        name: Radius-Server-1
        description: Radius-Server-1 desc
        id: RadiusServerGroupUUID
        type: RadiusServerGroup
        retryInterval: 4
        dynamicAuthorizationPort: 1800
        interimAccountUpdateInterval: 110
        groupAccountingMode: MULTIPLE
        realm: {'name': 'Realm', 'id': 'RealmUUID', 'type': 'Realm'}
        enableAuthorizeOnly: True
        enableInterimAccountUpdate: True
        enableDynamicAuthorization: True
        radiusServers: [{'timeout': 110, 'host': 'string', 'interface': {'name': 'String', 'id': 'InterfaceUUID', 'type': 'SecurityZone'}, 'serverSecretKey': '****', 'serverAuthenticationPort': 1812, 'serverAccountingPort': 1813, 'useRoutingToSelectInterface': True, 'redirectACL': {'name': 'string', 'id': 'ExtendedAccessListUUID', 'type': 'ExtendedAccessList'}}]
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```