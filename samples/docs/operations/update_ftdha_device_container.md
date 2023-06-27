# updateFTDHADeviceContainer

The updateFTDHADeviceContainer operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/devicehapairs/ftddevicehapairs/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/devicehapairs/ftddevicehapairs/{object_id}.md) path.&nbsp;
## Description
**Retrieves or modifies the Firewall Threat Defense HA record associated with the specified ID. Creates or breaks or deletes a Firewall Threat Defense HA pair. If no ID is specified for a GET, retrieves list of all Firewall Threat Defense HA pairs. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| id | ha_container_uuid |
| name | new_ha_name |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier of a Firewall Threat Defense HA pair. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'updateFTDHADeviceContainer' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateFTDHADeviceContainer"
    data:
        id: ha_container_uuid
        name: new_ha_name
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```