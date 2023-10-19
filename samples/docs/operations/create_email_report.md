# createEmailReport

The createEmailReport operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/deployment/jobhistories/{containerUUID}/operational/emailreports](/paths//api/fmc_config/v1/domain/{domain_uuid}/deployment/jobhistories/{container_uuid}/operational/emailreports.md) path.&nbsp;
## Description
**Emails the report _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| recipientList | ['mail1@cisco.com', 'mail2@cisco.com'] |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createEmailReport' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createEmailReport"
    data:
        recipientList: ['mail1@cisco.com', 'mail2@cisco.com']
    path_params:
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```