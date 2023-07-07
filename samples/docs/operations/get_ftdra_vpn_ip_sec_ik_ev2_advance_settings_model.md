# getFTDRAVpnIPSecIKEv2AdvanceSettingsModel

The getFTDRAVpnIPSecIKEv2AdvanceSettingsModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/ravpns/{containerUUID}/ipsecadvancedsettings/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/ravpns/{container_uuid}/ipsecadvancedsettings/{object_id}.md) path.&nbsp;
## Description
**Retrieves IPSec Advance Setting inside a VPN RA Topology. If no ID is specified for a GET, retrieves list containing a single IPSEC Advance Setting entry of the topology.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier for IPSec Advance Setting in a RA VPN topology. |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'getFTDRAVpnIPSecIKEv2AdvanceSettingsModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getFTDRAVpnIPSecIKEv2AdvanceSettingsModel"
    path_params:
        objectId: "{{ object_id }}"
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```