# createDownloadInternalCA

The createDownloadInternalCA operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/downloadinternalca](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/downloadinternalca.md) path.&nbsp;
## Description
**Retrieves and downloads the Internal CA object in a PKCS12 file encrypted using the provided password. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| id | 31cba922-9c1b-11ec-bbc8-d3a155c5f4d0 |
| password | password |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createDownloadInternalCA' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createDownloadInternalCA"
    data:
        id: 31cba922-9c1b-11ec-bbc8-d3a155c5f4d0
        password: password
    path_params:
        domainUUID: "{{ domain_uuid }}"

```