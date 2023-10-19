# createSecurityGroupTag

The createSecurityGroupTag operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/securitygrouptags](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/securitygrouptags.md) path.&nbsp;
## Description
**Retrieves the custom security group tag object associated with the specified ID. If no ID is specified, retrieves list of all custom security group tag objects. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| name | ExampleSGTname |
| tag | 23 |
| description | SGT description |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createSecurityGroupTag' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createSecurityGroupTag"
    data:
        name: ExampleSGTname
        tag: 23
        description: SGT description
    path_params:
        domainUUID: "{{ domain_uuid }}"

```