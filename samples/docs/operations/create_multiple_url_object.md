# createMultipleURLObject

The createMultipleURLObject operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/urls](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/urls.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the url objects associated with the specified ID. If no ID is specified, retrieves list of all url objects. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value | Description |
| --------- | -------- | -------- |
| type | Url | Type associated with resource: URL. |
| name | UrlObject1 | User chosen resource name. |
| description | url object 1 | Description |
| url | http://wwwin.cisco.com | Actual URL of object. |
| type | Url | Type associated with resource: URL. |
| name | UrlObject2 | User chosen resource name. |
| description | url object 2 | Descriptio |
| url | http://www.google.com | Actual URL of object. |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string | Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| bulk | False | boolean | Enables bulk create for url objects. |

## Example
```yaml
- name: Execute 'createMultipleURLObject' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createMultipleURLObject"
    data:
        type: "Url"
        name: "UrlObject1"
        description: "url object 1"
        url: "http://wwwin.cisco.com"
        type: "Url"
        name: "UrlObject2"
        description: "url object 2"
        url: "http://www.google.com"
    path_params:
        domainUUID: "{{ domain_uuid }}"
    query_params:
        bulk: "{{ bulk }}"

```
