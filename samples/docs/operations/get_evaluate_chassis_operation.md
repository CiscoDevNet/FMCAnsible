# getEvaluateChassisOperation

The getEvaluateChassisOperation operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/chassis/fmcmanagedchassis/{containerUUID}/chassisinterfaces/{interfaceUUID}/evaluateoperation](/paths//api/fmc_config/v1/domain/{domain_uuid}/chassis/fmcmanagedchassis/{container_uuid}/chassisinterfaces/{interface_uuid}/evaluateoperation.md) path.&nbsp;
## Description
**Validate interface usage**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| interfaceUUID | True | string <td colspan=3> Unique identifier of a chassis interface. |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| operationType | True | string <td colspan=3> Evaluate feasibility of chassis operation(BREAKOUT/JOIN). |
| offset | False | integer <td colspan=3> Index of first item to return. |
| limit | False | integer <td colspan=3> Number of items to return. |
| expanded | False | boolean <td colspan=3> If set to true, the GET response displays a list of objects with additional attributes. |

## Example
```yaml
- name: Execute 'getEvaluateChassisOperation' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getEvaluateChassisOperation"
    path_params:
        interfaceUUID: "{{ interface_uuid }}"
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"
    query_params:
        operationType: "{{ operation_type }}"
        offset: "{{ offset }}"
        limit: "{{ limit }}"
        expanded: "{{ expanded }}"

```