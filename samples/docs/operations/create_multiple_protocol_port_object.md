# createMultipleProtocolPortObject

The createMultipleProtocolPortObject operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/protocolportobjects](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/protocolportobjects.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the protocol(tcp/udp) port object associated with the specified ID. If no ID is specified for a GET, retrieves list of all protocol(tcp/udp) port objects. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value | Description |
| --------- | -------- | -------- |
| name | protocolport_obj1 | User chosen resource name. |
| protocol | TCP  | IANA protocol number or Ethertype. This is handled differently for Transport and Network layer protocols. Transport layer protocols are identified by the IANA protocol number. For example: • 6 — TCP • 17 — UDP Network layer protocols are identified by the decimal form of the IEEE Registration Authority Ethertype. For example: • 2048 — IP. |
| port | 123 | Port number for the object. |
| type | ProtocolPortObject | Type associated with resource: ProtocolPortObject |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string | Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| bulk | False | boolean | Enables bulk create for protocol port objects. |

## Example
```yaml
- name: Execute 'createMultipleProtocolPortObject' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createMultipleProtocolPortObject"
    data:
        name: "protocolport_obj1"
        protocol: "TCP"
        port: 123
        type: "ProtocolPortObject"
    path_params:
        domainUUID: "{{ domain_uuid }}"
    query_params:
        bulk: "{{ bulk }}"

```
