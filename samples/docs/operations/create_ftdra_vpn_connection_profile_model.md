# createFTDRAVpnConnectionProfileModel

The createFTDRAVpnConnectionProfileModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/ravpns/{containerUUID}/connectionprofiles](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/ravpns/{container_uuid}/connectionprofiles.md) path.&nbsp;
## Description
**Retrieves Connection Profile data inside a VPN RA Topology. If no ID is specified for a GET, retrieves list containing a single Connection Profile entry of the topology. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createFTDRAVpnConnectionProfileModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createFTDRAVpnConnectionProfileModel"
    path_params:
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```