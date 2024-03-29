# createExpandedCommunityList

The createExpandedCommunityList operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/expandedcommunitylists](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/expandedcommunitylists.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the ExpandedCommunityList object associated with the specified ID. If no ID is specified for a GET, retrieves list of all ExpandedCommunityList objects. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string | Domain UUID |

## Example
```yaml
- name: Execute 'createExpandedCommunityList' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createExpandedCommunityList"
    path_params:
        domainUUID: "{{ domain_uuid }}"

```
