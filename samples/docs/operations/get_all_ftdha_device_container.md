# getAllFTDHADeviceContainer

The getAllFTDHADeviceContainer operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/devicehapairs/ftddevicehapairs](/paths//api/fmc_config/v1/domain/{domain_uuid}/devicehapairs/ftddevicehapairs.md) path.&nbsp;
## Description
**Retrieves or modifies the Firewall Threat Defense HA record associated with the specified ID. Creates or breaks or deletes a Firewall Threat Defense HA pair. If no ID is specified for a GET, retrieves list of all Firewall Threat Defense HA pairs.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| filter | False | string <td colspan=3> Filter for analytics only HA<br/><code>analyticsOnly</code> -- Allowed values are <code>{true|false}</code><br/> |
| offset | False | integer <td colspan=3> Index of first item to return. |
| limit | False | integer <td colspan=3> Number of items to return. |
| expanded | False | boolean <td colspan=3> If set to true, the GET response displays a list of objects with additional attributes. |

## Example
```yaml
- name: Execute 'getAllFTDHADeviceContainer' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getAllFTDHADeviceContainer"
    path_params:
        domainUUID: "{{ domain_uuid }}"
    query_params:
        filter: "{{ filter }}"
        offset: "{{ offset }}"
        limit: "{{ limit }}"
        expanded: "{{ expanded }}"

```