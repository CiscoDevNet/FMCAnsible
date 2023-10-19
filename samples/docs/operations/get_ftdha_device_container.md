# getFTDHADeviceContainer

The getFTDHADeviceContainer operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/devicehapairs/ftddevicehapairs/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/devicehapairs/ftddevicehapairs/{object_id}.md) path.&nbsp;
## Description
**Retrieves or modifies the Firewall Threat Defense HA record associated with the specified ID. Creates or breaks or deletes a Firewall Threat Defense HA pair. If no ID is specified for a GET, retrieves list of all Firewall Threat Defense HA pairs.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier of a Firewall Threat Defense HA pair. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'getFTDHADeviceContainer' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getFTDHADeviceContainer"
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```