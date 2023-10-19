# createFTDRAVpnModel

The createFTDRAVpnModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/ravpns](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/ravpns.md) path.&nbsp;
## Description
**Retrieves the Firewall Threat Defense RA VPN topology associated with the specified ID. If no ID is specified for a GET, retrieves list of all Firewall Threat Defense RA VPN topologies. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createFTDRAVpnModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createFTDRAVpnModel"
    path_params:
        domainUUID: "{{ domain_uuid }}"

```