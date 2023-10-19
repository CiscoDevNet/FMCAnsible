# createValidateCertFile

The createValidateCertFile operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/validatecertfile](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/validatecertfile.md) path.&nbsp;
## Description
**Uploads and parses a given certificate/key file. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| payloadFile | X.509 Certificate file |
| fileType | CERT |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createValidateCertFile' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createValidateCertFile"
    data:
        payloadFile: X.509 Certificate file
        fileType: CERT
    path_params:
        domainUUID: "{{ domain_uuid }}"

```