# getFTDRAVpnLDAPAttributeModel

The getFTDRAVpnLDAPAttributeModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/ravpns/{containerUUID}/ldapattributemaps/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/ravpns/{container_uuid}/ldapattributemaps/{object_id}.md) path.&nbsp;
## Description
**Retrieves LDAP Attribute Maps inside a VPN RA Topology. If no ID is specified for a GET, retrieves list containing a single LDAP Attribute Maps of the topology.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier for LDAP Attribute Maps in a RA VPN topology. |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'getFTDRAVpnLDAPAttributeModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getFTDRAVpnLDAPAttributeModel"
    path_params:
        objectId: "{{ object_id }}"
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```