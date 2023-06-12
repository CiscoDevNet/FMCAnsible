# createPacketTracerPCAP

The createPacketTracerPCAP operation handles configuration related to [/api/fmc_troubleshoot/v1/domain/{domainUUID}/packettracer/pcaptraces](/paths//api/fmc_troubleshoot/v1/domain/{domain_uuid}/packettracer/pcaptraces.md) path.&nbsp;
## Description
**Retrieves the Packet Tracer using a PCAP file command output for FTD. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value | Description |
| --------- | -------- | -------- |
| device | {'id': '005056B1-FFEF-0ed3-0000-004294968641', 'type': 'Device', 'name': 'Device_A'} | 'id': 'Unique identifier representing resource', 'type': 'Response object associated with resource: Device', 'name': 'User chosen resource name.' |
| interface | {'id': '005056B1-FFEF-0ed3-0000-004294968640', 'type': 'PhysicalInterface', 'name': 'Management'} | 'id': 'Unique identifier representing resource', 'type': 'Response object associated with resource: PhysicalInterface', 'name': 'User chosen resource name.' |
| pcapFileName | UDP.pcap | Represents the name of a previously uploaded PCAP file on FMC. |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string | Domain UUID |

## Example
```yaml
- name: Execute 'createPacketTracerPCAP' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createPacketTracerPCAP"
    data:
        device: {'id': '005056B1-FFEF-0ed3-0000-004294968641', 'type': 'Device', 'name': 'Device_A'}
        interface: {'id': '005056B1-FFEF-0ed3-0000-004294968640', 'type': 'PhysicalInterface', 'name': 'Management'}
        pcapFileName: "UDP.pcap"
    path_params:
        domainUUID: "{{ domain_uuid }}"

```
