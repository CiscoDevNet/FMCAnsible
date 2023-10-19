# createPolicyLock

The createPolicyLock operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/operational/policylocks](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/operational/policylocks.md) path.&nbsp;
## Description
**Locks or unlocks the policy. Currently supports only Access policy. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| policies | [{'lock': 'true', 'policy': {'id': 'String', 'type': 'AccessPolicy'}}] |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createPolicyLock' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createPolicyLock"
    data:
        policies: [{'lock': 'true', 'policy': {'id': 'String', 'type': 'AccessPolicy'}}]
    path_params:
        domainUUID: "{{ domain_uuid }}"

```