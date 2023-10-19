# createTerminateRAVPNSession

The createTerminateRAVPNSession operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/health/ravpnsessions/operational/terminateravpnsessions](/paths//api/fmc_config/v1/domain/{domain_uuid}/health/ravpnsessions/operational/terminateravpnsessions.md) path.&nbsp;
## Description
**&#91;DEV ERROR: Missing description&#93; _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createTerminateRAVPNSession' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createTerminateRAVPNSession"
    path_params:
        domainUUID: "{{ domain_uuid }}"

```