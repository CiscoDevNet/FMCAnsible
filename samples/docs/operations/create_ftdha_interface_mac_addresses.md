# createFTDHAInterfaceMACAddresses

The createFTDHAInterfaceMACAddresses operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/devicehapairs/ftddevicehapairs/{containerUUID}/failoverinterfacemacaddressconfigs](/paths//api/fmc_config/v1/domain/{domain_uuid}/devicehapairs/ftddevicehapairs/{container_uuid}/failoverinterfacemacaddressconfigs.md) path.&nbsp;
## Description
**Retrieves or modifies the Firewall Threat Defense HA failover policy interface MAC addresses record associated with the specified Firewall Threat Defense HA pair. If no ID is specified for a GET, retrieves list of all Firewall Threat Defense HA failover policy interface MAC addresses records. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createFTDHAInterfaceMACAddresses' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createFTDHAInterfaceMACAddresses"
    path_params:
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```