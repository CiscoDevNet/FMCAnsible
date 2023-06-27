# getUmbrellaDNSPolicy

The getUmbrellaDNSPolicy operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/umbrelladnspolicies/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/umbrelladnspolicies/{object_id}.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the umbrella DNS policy associated with the specified ID. Also, retrieves list of all umbrella DNS policies.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier for umbrella DNS policy. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'getUmbrellaDNSPolicy' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getUmbrellaDNSPolicy"
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```