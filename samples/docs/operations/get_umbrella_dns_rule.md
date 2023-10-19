# getUmbrellaDNSRule

The getUmbrellaDNSRule operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/umbrelladnspolicies/{containerUUID}/umbrelladnsrules/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/umbrelladnspolicies/{container_uuid}/umbrelladnsrules/{object_id}.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the umbrella DNS Rule associated with the specified ID. Also, retrieves list of all umbrella DNS rules.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier for umbrella DNS rule. |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'getUmbrellaDNSRule' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getUmbrellaDNSRule"
    path_params:
        objectId: "{{ object_id }}"
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```