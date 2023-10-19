# createEBSSnapshot

The createEBSSnapshot operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/integration/ebssnapshot](/paths//api/fmc_config/v1/domain/{domain_uuid}/integration/ebssnapshot.md) path.&nbsp;
## Description
**Retrieves or creates an EBS snapshot. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createEBSSnapshot' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createEBSSnapshot"
    path_params:
        domainUUID: "{{ domain_uuid }}"

```