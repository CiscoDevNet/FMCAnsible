# updateFTDRAVpnIPSecIKEv2AdvanceSettingsModel

The updateFTDRAVpnIPSecIKEv2AdvanceSettingsModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/ravpns/{containerUUID}/ipsecadvancedsettings/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/ravpns/{container_uuid}/ipsecadvancedsettings/{object_id}.md) path.&nbsp;
## Description
**Retrieves IPSec Advance Setting inside a VPN RA Topology. If no ID is specified for a GET, retrieves list containing a single IPSEC Advance Setting entry of the topology. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| type | RaVpnIPsecAdvancedSetting |
| ipsecsettings | {'maximumTransmissionUnitAging': {'enabled': False, 'resetIntervalMinutes': 1}, 'enableFragmentationBeforeEncryption': True} |
| natKeepaliveMessageTraversal | {'enabled': True, 'intervalSeconds': 20} |
| ikev2settings | {'cookieChallenge': 'NEVER', 'identitySentToPeer': 'AUTO_OR_DN', 'enableNotificationOnTunnelDisconnect': False, 'doNotRebootUntilSessionsTerminated': False, 'thresholdToChallengeIncomingCookies': 50, 'percentageOfSAsAllowedInNegotiation': 100, 'maximumNumberOfSAsAllowed': 1} |
| id | 00505681-968B-0ed3-0000-008589934846 |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier for IPSec Advance Setting in a RA VPN topology. |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'updateFTDRAVpnIPSecIKEv2AdvanceSettingsModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateFTDRAVpnIPSecIKEv2AdvanceSettingsModel"
    data:
        type: RaVpnIPsecAdvancedSetting
        ipsecsettings: {'maximumTransmissionUnitAging': {'enabled': False, 'resetIntervalMinutes': 1}, 'enableFragmentationBeforeEncryption': True}
        natKeepaliveMessageTraversal: {'enabled': True, 'intervalSeconds': 20}
        ikev2settings: {'cookieChallenge': 'NEVER', 'identitySentToPeer': 'AUTO_OR_DN', 'enableNotificationOnTunnelDisconnect': False, 'doNotRebootUntilSessionsTerminated': False, 'thresholdToChallengeIncomingCookies': 50, 'percentageOfSAsAllowedInNegotiation': 100, 'maximumNumberOfSAsAllowed': 1}
        id: 00505681-968B-0ed3-0000-008589934846
    path_params:
        objectId: "{{ object_id }}"
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```