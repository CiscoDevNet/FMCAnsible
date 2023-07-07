# updateFTDRAVpnAddressAssignmentSetting

The updateFTDRAVpnAddressAssignmentSetting operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/ravpns/{containerUUID}/addressassignmentsettings/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/ravpns/{container_uuid}/addressassignmentsettings/{object_id}.md) path.&nbsp;
## Description
**Retrieves Address Assignment Setting inside a VPN RA Topology. If no ID is specified for a GET, retrieves list containing a single Address Assignment Setting entry of the topology. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| type | RaVpnAddressAssignmentSetting |
| useAuthorizationServerForIPv4 | True |
| useDHCP | True |
| useInternalAddressPoolForIPv4 | True |
| ipAddressReuseInterval | 10 |
| useAuthorizationServerForIPv6 | True |
| useInternalAddressPoolForIPv6 | True |
| id | 00505681-968B-0ed3-0000-150323855419 |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier for Address Assignment Setting in a RA VPN topology. |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'updateFTDRAVpnAddressAssignmentSetting' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateFTDRAVpnAddressAssignmentSetting"
    data:
        type: RaVpnAddressAssignmentSetting
        useAuthorizationServerForIPv4: True
        useDHCP: True
        useInternalAddressPoolForIPv4: True
        ipAddressReuseInterval: 10
        useAuthorizationServerForIPv6: True
        useInternalAddressPoolForIPv6: True
        id: 00505681-968B-0ed3-0000-150323855419
    path_params:
        objectId: "{{ object_id }}"
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```