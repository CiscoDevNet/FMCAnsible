# createIntrusionPolicy

The createIntrusionPolicy operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/intrusionpolicies](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/intrusionpolicies.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the intrusion policy associated with the specified ID. Also, retrieves list of all intrusion policies. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value | Description |
| --------- | -------- | ----------- |
| basePolicy | {'name': 'test1', 'id': 'intrusionPolicyUUID', 'type': 'IntrusionPolicy'} | Base Policy (User chosen resource name, Unique identifier representing resource, Response object associated with resource) |
| description | Created via automation | Description of the Intrusion Policy. |
| inspectionMode | PREVENTION(defaultAction), DETECTION. |  Indicates the inspection mode. Can be either DETECTION or PREVENTION. Only applicable for Snort 3 engine.|
| name | test1 | Name of the Intrusion Policy. |
| type | IntrusionPolicy | Type of the object. This value is always 'intrusionpolicy'. |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string | Domain UUID |

## Example
```yaml
- name: Execute 'createIntrusionPolicy' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createIntrusionPolicy"
    data:
        basePolicy: {'name': 'test1', 'id': 'intrusionPolicyUUID', 'type': 'IntrusionPolicy'}
        description: "Created via automation"
        inspectionMode: "PREVENTION"
        name: "test1"
        type: "IntrusionPolicy"
    path_params:
        domainUUID: "{{ domain_uuid }}"

```
