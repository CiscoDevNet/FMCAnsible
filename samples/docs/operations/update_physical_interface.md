# updatePhysicalInterface

The updatePhysicalInterface operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/chassis/fmcmanagedchassis/{containerUUID}/physicalinterfaces/{interfaceUUID}](/paths//api/fmc_config/v1/domain/{domain_uuid}/chassis/fmcmanagedchassis/{container_uuid}/physicalinterfaces/{interface_uuid}.md) path.&nbsp;
## Description
**Retrieves or modifies the chassis Physical interface configurations. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| id | networkModuleUUID |
| moduleState | DISABLED |
| type | NetworkModule |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| interfaceUUID | True | string <td colspan=3> Unique identifier of a chassis physical interface. |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'updatePhysicalInterface' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updatePhysicalInterface"
    data:
        id: networkModuleUUID
        moduleState: DISABLED
        type: NetworkModule
    path_params:
        interfaceUUID: "{{ interface_uuid }}"
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```