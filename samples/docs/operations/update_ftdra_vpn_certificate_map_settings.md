# updateFTDRAVpnCertificateMapSettings

The updateFTDRAVpnCertificateMapSettings operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/ravpns/{containerUUID}/certificatemapsettings/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/ravpns/{container_uuid}/certificatemapsettings/{object_id}.md) path.&nbsp;
## Description
**Retrieves Certificate Map Setting inside a VPN RA Topology. If no ID is specified for a GET, retrieves list containing a single Certificate Map Setting entry of the topology. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| type | RaVpnCertificateMapSetting |
| useGroupURL | True |
| enableCertificateToConnectionProfileMapping | True |
| certificateToConnectionProfileMap | [{'certificateMap': {'id': 'certMapNameUUID', 'type': 'CertificateMap', 'name': 'certMapName'}, 'connectionProfile': {'id': 'connectionProfileUUID', 'type': 'RaVpnConnectionProfile', 'name': 'connProfileName'}}] |
| id | 00505681-CCB3-0ed3-0000-017179869352 |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier for Certificate Map Setting in a RA VPN topology. |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'updateFTDRAVpnCertificateMapSettings' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateFTDRAVpnCertificateMapSettings"
    data:
        type: RaVpnCertificateMapSetting
        useGroupURL: True
        enableCertificateToConnectionProfileMapping: True
        certificateToConnectionProfileMap: [{'certificateMap': {'id': 'certMapNameUUID', 'type': 'CertificateMap', 'name': 'certMapName'}, 'connectionProfile': {'id': 'connectionProfileUUID', 'type': 'RaVpnConnectionProfile', 'name': 'connProfileName'}}]
        id: 00505681-CCB3-0ed3-0000-017179869352
    path_params:
        objectId: "{{ object_id }}"
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```