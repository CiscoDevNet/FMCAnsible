# getAllTaskStatus

The getAllTaskStatus operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/job/taskstatuses](/paths//api/fmc_config/v1/domain/{domain_uuid}/job/taskstatuses.md) path.&nbsp;
## Description
**Retrieves information about a previously submitted pending job/task with the specified ID.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| filter | True | string <td colspan=3> Filter criteria can be specified using the format <code>type:{type};status:{status};</code>.  <br/><br/><code>type</code> -- Type of task to be returned. It is mandatory field. Allowed values are <code>"{Deployment | Registration | Unregistration}"</code>. <br/><br/><code>status</code> -- Filter based on the status of the task. It is mandatory field.<br/><br/>&emsp;Allowed values for <code>Deployment</code> task are <code>"{Deploying | Cancelled | Failed | Succeeded}"</code>.<br/><br/>&emsp;Allowed values for <code>Registration</code> task are <code>"{Pending | Running | Success | Failed}"</code>.<br/><br/>&emsp;Allowed values for <code>Unregistration</code> task are <code>"{Running | Success | Failed}"</code>. |
| offset | False | integer <td colspan=3> Index of first item to return. |
| limit | False | integer <td colspan=3> Number of items to return. |
| expanded | False | boolean <td colspan=3> If set to true, the GET response displays a list of objects with additional attributes. |

## Example
```yaml
- name: Execute 'getAllTaskStatus' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getAllTaskStatus"
    path_params:
        domainUUID: "{{ domain_uuid }}"
    query_params:
        filter: "{{ filter }}"
        offset: "{{ offset }}"
        limit: "{{ limit }}"
        expanded: "{{ expanded }}"

```