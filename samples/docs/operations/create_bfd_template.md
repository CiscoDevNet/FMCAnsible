# createBFDTemplate

The createBFDTemplate operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/bfdtemplates](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/bfdtemplates.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the BFDTemplate object associated with the specified ID. If no ID is specified for a GET, retrieves list of all Bidirectional Forwarding Detection routing template objects. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| type | BFDTemplate |
| name | singleHopTemplateAlpha |
| hopType | SINGLE_HOP |
| echo | ENABLED |
| txRxInterval | MILLISECONDS |
| txRxMultiplier | 5 |
| minTransmit | 51 |
| minReceive | 52 |
| authentication | {'authType': 'MD5', 'pwdEncryption': 'UN_ENCRYPTED', 'authKey': 'Admin@123', 'authKeyId': 1} |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createBFDTemplate' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createBFDTemplate"
    data:
        type: BFDTemplate
        name: singleHopTemplateAlpha
        hopType: SINGLE_HOP
        echo: ENABLED
        txRxInterval: MILLISECONDS
        txRxMultiplier: 5
        minTransmit: 51
        minReceive: 52
        authentication: {'authType': 'MD5', 'pwdEncryption': 'UN_ENCRYPTED', 'authKey': 'Admin@123', 'authKeyId': 1}
    path_params:
        domainUUID: "{{ domain_uuid }}"

```