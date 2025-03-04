# updateIKEv2IPsecProposal

The updateIKEv2IPsecProposal operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/ikev2ipsecproposals/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/ikev2ipsecproposals/{object_id}.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the IKEv2 IPSec Proposal associated with the specified ID. If no ID is specified for a GET, retrieves list of all IKEv2 IPSec Proposal objects. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| name | ikev2ipsecproposal-test-1 |
| id | ikev2ipsecproposalUUID |
| encryptionAlgorithms | ['3DES'] |
| integrityAlgorithms | ['SHA-256'] |
| type | IKEv2IPsecProposal |
| description | IKEv2 IPsec object description |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier for IKEv2 IPSec Proposal object. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'updateIKEv2IPsecProposal' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateIKEv2IPsecProposal"
    data:
        name: ikev2ipsecproposal-test-1
        id: ikev2ipsecproposalUUID
        encryptionAlgorithms: ['3DES']
        integrityAlgorithms: ['SHA-256']
        type: IKEv2IPsecProposal
        description: IKEv2 IPsec object description
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```