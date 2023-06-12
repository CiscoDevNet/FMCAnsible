# createDevice

The createDevice operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords](/paths//api/fmc_config/v1/domain/{domain_uuid}/devices/devicerecords.md) path.&nbsp;
## Description
**Retrieves or modifies the device record associated with the specified ID. Registers or unregisters a device. If no ID is specified for a GET, retrieves list of all device records. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value | Description |
| --------- | -------- | -------- |
| name | <name> | User-specified name of the registered device. (Example: Device 01 - 192.168.0.152.) |
| hostName | <host name> | Hostname or IP address of the device. If the device is behind NAT, you can leave the host name as blank, and enter the NAT_ID string in the 'Unique NAT ID' text box. Use the same NAT_ID string that you used while configuring FMC on the device. |
| natID | cisco123 | Unique ID for a Network address translation (NAT) device (optional; used for device registration). If the device to be registered and the Firepower Management Center are separated by a NAT device, enter a unique NAT ID. |
| regKey | regkey | Registration Key that you entered while configuring FMC on the device. |
| type | Device | Type of the device; this value is always Device. |
| license_caps | ['MALWARE', 'URLFilter', 'PROTECT', 'CONTROL', 'VPN'] | Array of strings representing the license capabilities on the managed device. For registering FTD, the allowed values are: ESSENTIALS (mandatory), IPS, URL, MALWARE_DEFENSE, CARRIER, SECURE_CLIENT_PREMIER, SECURE_CLIENT_PREMIER_ADVANTAGE, SECURE_CLIENT_VPNOnly. For Firepower ASA or NGIPSv devices, allowed values are: BASE, THREAT, PROTECT, CONTROL, URLFilter, MALWARE, VPN, SSL. |
| accessPolicy | {'id': 'accessPolicyUUID', 'type': 'AccessPolicy'} | AccessPolicy ID |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string | Domain UUID |

## Example
```yaml
- name: Execute 'createDevice' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createDevice"
    data:
        name: "<name>"
        hostName: "<host name>"
        natID: "cisco123"
        regKey: "regkey"
        type: "Device"
        license_caps: ['MALWARE', 'URLFilter', 'PROTECT', 'CONTROL', 'VPN']
        accessPolicy: {'id': 'accessPolicyUUID', 'type': 'AccessPolicy'}
    path_params:
        domainUUID: "{{ domain_uuid }}"

```
