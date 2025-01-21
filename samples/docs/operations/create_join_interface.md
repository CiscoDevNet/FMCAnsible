# createJoinInterface

The createJoinInterface operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/chassis/fmcmanagedchassis/{containerUUID}/operational/joininterfaces](/paths//api/fmc_config/v1/domain/{domain_uuid}/chassis/fmcmanagedchassis/{container_uuid}/operational/joininterfaces.md) path.&nbsp;
## Description
**Join interface. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| ignoreWarning | False | boolean <td colspan=3> Ignore the warning alerts for the Join operation |

## Example
```yaml
- name: Execute 'createJoinInterface' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createJoinInterface"
    path_params:
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"
    query_params:
        ignoreWarning: "{{ ignore_warning }}"

```