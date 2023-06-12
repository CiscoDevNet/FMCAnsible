# createPacketTracerPCAPFiles

The createPacketTracerPCAPFiles operation handles configuration related to [/api/fmc_troubleshoot/v1/domain/{domainUUID}/packettracer/files](/paths//api/fmc_troubleshoot/v1/domain/{domain_uuid}/packettracer/files.md) path.&nbsp;
## Description
**Creates, deletes, or retrieves PCAP files from FMC. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value | Description |
| --------- | -------- | -------- |
| payloadFile | .pcap or .pcapng file | Select a PCAP file. .pcap and .pcapng are the supported file formats. *required |
| replaceFile | true or false | Replaces the file on disk if it already exists. By default is set to false. |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string | Domain UUID |

## Example
```yaml
- name: Execute 'createPacketTracerPCAPFiles' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createPacketTracerPCAPFiles"
    data:
        payloadFile: ".pcap or .pcapng file"
        replaceFile: "true or false"
    path_params:
        domainUUID: "{{ domain_uuid }}"

```
