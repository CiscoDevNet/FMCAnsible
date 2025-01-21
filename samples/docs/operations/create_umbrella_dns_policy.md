# createUmbrellaDNSPolicy

The createUmbrellaDNSPolicy operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/umbrelladnspolicies](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/umbrelladnspolicies.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the umbrella DNS policy associated with the specified ID. Also, retrieves list of all umbrella DNS policies. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| type | UmbrellaDNSPolicy |
| name | Umbrella DNS Policy |
| description | Umbrella DNS policy for testing rest API |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createUmbrellaDNSPolicy' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createUmbrellaDNSPolicy"
    data:
        type: UmbrellaDNSPolicy
        name: Umbrella DNS Policy
        description: Umbrella DNS policy for testing rest API
    path_params:
        domainUUID: "{{ domain_uuid }}"

```