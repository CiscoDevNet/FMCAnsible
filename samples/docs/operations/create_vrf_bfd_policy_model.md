# createVrfBFDPolicyModel

The createVrfBFDPolicyModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/devices/devicerecords/{containerUUID}/routing/virtualrouters/{virtualrouterUUID}/bfdpolicies](/paths//api/fmc_config/v1/domain/{domain_uuid}/devices/devicerecords/{container_uuid}/routing/virtualrouters/{virtualrouter_uuid}/bfdpolicies.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the BFD Policy associated with the specified ID. If no ID is specified for a GET, retrieves list of all BFD Policies. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| type | BFDPolicy |
| hopType | SINGLE_HOP |
| interface | {'id': 'interface_uuid', 'type': 'PhysicalInterface', 'name': 'GigabitEthernet1/1'} |
| template | {'id': 'template_uuid', 'type': 'BFDTemplate', 'name': 'SingleHopTemplate1'} |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| virtualrouterUUID | True | string <td colspan=3> Unique identifier of Virtual Router. |
| containerUUID | True | string <td colspan=3> The container id under which this specific resource is contained. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createVrfBFDPolicyModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createVrfBFDPolicyModel"
    data:
        type: BFDPolicy
        hopType: SINGLE_HOP
        interface: {'id': 'interface_uuid', 'type': 'PhysicalInterface', 'name': 'GigabitEthernet1/1'}
        template: {'id': 'template_uuid', 'type': 'BFDTemplate', 'name': 'SingleHopTemplate1'}
    path_params:
        virtualrouterUUID: "{{ virtualrouter_uuid }}"
        containerUUID: "{{ container_uuid }}"
        domainUUID: "{{ domain_uuid }}"

```