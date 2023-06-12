# createECMPZoneModel

The createECMPZoneModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/ecmpzones](/paths//api/fmc_config/v1/domain/{domain_uuid}/devices/devicerecords/{container_uuid}/routing/ecmpzones.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the ECMP Zone associated with the specified ID. Also, retrieves list of all ECMP Zone.  _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value | Description |
| --------- | -------- | -------- |
| type | ecmpzones | Type of the ECMP Zone. This value is always ecmpzones |
| name | ECMPZoneBeta | ECMP Zone Name |
| description | ECMP Zone Beta | Description of Equal-Cost Multi-Path (ECMP) Zone |
| interfaces | [{'id': 'interface_uuid1', 'type': 'PhysicalInterface', 'name': 'GigabitEthernet1/1'}, {'id': 'interface_uuid2', 'type': 'PhysicalInterface', 'name': 'GigabitEthernet1/2'}] | List of interfaces to be associated with ECMP Zone |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| containerUUID | True | string | The container id under which this specific resource is contained. |
| domainUUID | True | string | Domain UUID |

## Example
```yaml
- name: Execute 'createECMPZoneModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createECMPZoneModel"
    data:
        type: "ecmpzones"
        name: "ECMPZoneBeta"
        description: "ECMP Zone Beta"
        interfaces: [{'id': 'interface_uuid1', 'type': 'PhysicalInterface', 'name': 'GigabitEthernet1/1'}, {'id': 'interface_uuid2', 'type': 'PhysicalInterface', 'name': 'GigabitEthernet1/2'}]
    path_params:
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```
