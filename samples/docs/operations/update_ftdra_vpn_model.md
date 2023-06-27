# updateFTDRAVpnModel

The updateFTDRAVpnModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/ravpns/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/ravpns/{object_id}.md) path.&nbsp;
## Description
**Retrieves the Firewall Threat Defense RA VPN topology associated with the specified ID. If no ID is specified for a GET, retrieves list of all Firewall Threat Defense RA VPN topologies. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| id | UUID |
| name | Name |
| type | RAVpn |
| description | SAMPLE PUT |
| configureSSL | True |
| configureIpsec | True |
| accessInterfaceSettings | {'bypassACPolicyForDecryptTraffic': False, 'interfaceSettings': [{'accessInterface': {'name': 'Name', 'id': 'UUID', 'type': 'SecurityZone'}, 'configureInterfaceIDCertificate': False, 'enableSSL': True, 'enableIPSecIkev2': True, 'enableDTLS': True}], 'webPort': 443, 'sslIdCertificate': {'type': 'CertEnrollment', 'name': 'Name', 'id': 'UUID'}, 'ipsecIdCertificate': {'type': 'CertEnrollment', 'name': 'Name', 'id': 'UUID'}, 'allowConnectionProfileSelection': True, 'dtlsPort': 443} |
| groupPolicies | [{'type': 'GroupPolicy', 'name': 'Name', 'id': 'UUID'}] |
| anyConnectClientImages | [{'operatingSystem': 'Windows', 'anyconnectImage': {'name': 'Name', 'type': 'AnyConnectPackage', 'id': 'UUID'}}] |
| externalBrowserPackage | {'name': 'Name', 'type': 'AnyConnectExternalBrowserPackage', 'id': 'UUID'} |
| dapPolicy | {'name': 'Name', 'id': 'UUID', 'type': 'DynamicAccessPolicy'} |
| localRealmServer | {'name': 'Name', 'id': 'UUID', 'type': 'IdentityRealm'} |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier for Firewall Threat Defense RA VPN topology. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'updateFTDRAVpnModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateFTDRAVpnModel"
    data:
        id: UUID
        name: Name
        type: RAVpn
        description: SAMPLE PUT
        configureSSL: True
        configureIpsec: True
        accessInterfaceSettings: {'bypassACPolicyForDecryptTraffic': False, 'interfaceSettings': [{'accessInterface': {'name': 'Name', 'id': 'UUID', 'type': 'SecurityZone'}, 'configureInterfaceIDCertificate': False, 'enableSSL': True, 'enableIPSecIkev2': True, 'enableDTLS': True}], 'webPort': 443, 'sslIdCertificate': {'type': 'CertEnrollment', 'name': 'Name', 'id': 'UUID'}, 'ipsecIdCertificate': {'type': 'CertEnrollment', 'name': 'Name', 'id': 'UUID'}, 'allowConnectionProfileSelection': True, 'dtlsPort': 443}
        groupPolicies: [{'type': 'GroupPolicy', 'name': 'Name', 'id': 'UUID'}]
        anyConnectClientImages: [{'operatingSystem': 'Windows', 'anyconnectImage': {'name': 'Name', 'type': 'AnyConnectPackage', 'id': 'UUID'}}]
        externalBrowserPackage: {'name': 'Name', 'type': 'AnyConnectExternalBrowserPackage', 'id': 'UUID'}
        dapPolicy: {'name': 'Name', 'id': 'UUID', 'type': 'DynamicAccessPolicy'}
        localRealmServer: {'name': 'Name', 'id': 'UUID', 'type': 'IdentityRealm'}
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```