# updateFTDRAVpnLDAPAttributeModel

The updateFTDRAVpnLDAPAttributeModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/ravpns/{containerUUID}/ldapattributemaps/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/ravpns/{container_uuid}/ldapattributemaps/{object_id}.md) path.&nbsp;
## Description
**Retrieves LDAP Attribute Maps inside a VPN RA Topology. If no ID is specified for a GET, retrieves list containing a single LDAP Attribute Maps of the topology. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| type | RaVpnLdapAttributeMap |
| ldapAttributeMapList | [{'realm': {'name': 'realm_1', 'id': '5dac6c26-5421-11ec-97cd-b79efba416a2', 'type': 'Realm'}, 'ldapAttributeMaps': [{'ldapName': 'department', 'ciscoName': 'Group-Policy', 'valueMappings': [{'type': 'LdapToGroupPolicyMapping', 'ldapValue': 'name', 'groupPolicy': {'name': 'group_2', 'id': '00505681-303E-0ed3-0000-549755813894', 'type': 'GroupPolicy'}}, {'type': 'LdapToGroupPolicyMapping', 'ldapValue': 'test', 'groupPolicy': {'name': 'group_policy_1', 'id': '00505681-303E-0ed3-0000-098784247856', 'type': 'GroupPolicy'}}]}, {'ldapName': 'mail', 'ciscoName': 'Banner_rest', 'valueMappings': [{'type': 'LdapToCiscoValueMapping', 'ciscoValue': 'test banner', 'ldapValue': 'attr'}]}]}] |
| id | 00505681-303E-0ed3-0000-004294968318 |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier for LDAP Attribute Maps in a RA VPN topology. |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'updateFTDRAVpnLDAPAttributeModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateFTDRAVpnLDAPAttributeModel"
    data:
        type: RaVpnLdapAttributeMap
        ldapAttributeMapList: [{'realm': {'name': 'realm_1', 'id': '5dac6c26-5421-11ec-97cd-b79efba416a2', 'type': 'Realm'}, 'ldapAttributeMaps': [{'ldapName': 'department', 'ciscoName': 'Group-Policy', 'valueMappings': [{'type': 'LdapToGroupPolicyMapping', 'ldapValue': 'name', 'groupPolicy': {'name': 'group_2', 'id': '00505681-303E-0ed3-0000-549755813894', 'type': 'GroupPolicy'}}, {'type': 'LdapToGroupPolicyMapping', 'ldapValue': 'test', 'groupPolicy': {'name': 'group_policy_1', 'id': '00505681-303E-0ed3-0000-098784247856', 'type': 'GroupPolicy'}}]}, {'ldapName': 'mail', 'ciscoName': 'Banner_rest', 'valueMappings': [{'type': 'LdapToCiscoValueMapping', 'ciscoValue': 'test banner', 'ldapValue': 'attr'}]}]}]
        id: 00505681-303E-0ed3-0000-004294968318
    path_params:
        objectId: "{{ object_id }}"
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```