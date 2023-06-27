# updateUmbrellaDNSRule

The updateUmbrellaDNSRule operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/umbrelladnspolicies/{containerUUID}/umbrelladnsrules/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/umbrelladnspolicies/{container_uuid}/umbrelladnsrules/{object_id}.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the umbrella DNS Rule associated with the specified ID. Also, retrieves list of all umbrella DNS rules. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| localByPassDomain | Domain for local bypass2 |
| isDNSCryptEnabled | True |
| umbrellaTag | Umbrella cloud tag2 |
| idleTimeOut | idle timeouts2 |
| id | umbrelladnsruleUUID2 |
| type | UmbrellaDNSRule |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier for umbrella DNS rule. |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'updateUmbrellaDNSRule' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateUmbrellaDNSRule"
    data:
        localByPassDomain: Domain for local bypass2
        isDNSCryptEnabled: True
        umbrellaTag: Umbrella cloud tag2
        idleTimeOut: idle timeouts2
        id: umbrelladnsruleUUID2
        type: UmbrellaDNSRule
    path_params:
        objectId: "{{ object_id }}"
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```