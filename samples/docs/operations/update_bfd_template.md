# updateBFDTemplate

The updateBFDTemplate operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/bfdtemplates/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/bfdtemplates/{object_id}.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the BFDTemplate object associated with the specified ID. If no ID is specified for a GET, retrieves list of all Bidirectional Forwarding Detection routing template objects. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| type | BFDTemplate |
| hopType | SINGLE_HOP |
| name | singleHopTemplateAlpha |
| echo | ENABLED |
| txRxInterval | MILLISECONDS |
| txRxMultiplier | 5 |
| minTransmit | 51 |
| minReceive | 52 |
| authentication | {'authType': 'MD5', 'pwdEncryption': 'UN_ENCRYPTED', 'authKey': 'Admin@123', 'authKeyId': 1} |
| id | BFDTemplateUUID |
| overridable | False |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier for BFDTemplate object. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'updateBFDTemplate' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateBFDTemplate"
    data:
        type: BFDTemplate
        hopType: SINGLE_HOP
        name: singleHopTemplateAlpha
        echo: ENABLED
        txRxInterval: MILLISECONDS
        txRxMultiplier: 5
        minTransmit: 51
        minReceive: 52
        authentication: {'authType': 'MD5', 'pwdEncryption': 'UN_ENCRYPTED', 'authKey': 'Admin@123', 'authKeyId': 1}
        id: BFDTemplateUUID
        overridable: False
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```