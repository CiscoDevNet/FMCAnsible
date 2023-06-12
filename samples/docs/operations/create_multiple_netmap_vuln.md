# createMultipleNetmapVuln

The createMultipleNetmapVuln operation handles configuration related to [/api/fmc_netmap/v1/domain/{domainUUID}/vulns](/paths//api/fmc_netmap/v1/domain/{domain_uuid}/vulns.md) path.&nbsp;
## Description
**Creates, deletes, or retrieves a vulnerability in the Network Map _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value | Description |
| --------- | -------- | ----------- |
| id | 12345 | ID of the vuln. When provided during creation, must be less than 2,000,000.
If not provided during creation, will be auto-assigned to a value greater than or equal to 2,000,000 |
| type | Vuln |  |
| ipAddress | 192.168.1.2 | IP address of the host that contains the vuln |
| source | MyVulnSource | Name of the source of the vulnerability. This groups together vulns from a single source.
Vulns discovered using passive detection (from a NGFW/NGIPS device) have the source as 'RNA' |
| cve | 2021-12345 | The CVE number of the vuln (eg. 2020-1234) |
| description | Description of the vuln | The description of the vuln. If this value is empty, the description is automatically taken from the title of the CVE |
| protocol | tcp | The protocol associated with the vuln. Can be: tcp or udp. If provided, must also provide a port |
| port | 443 | The port associated with the vuln. If provided, must also provide a protocol |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string | Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| bulk | False | boolean | Enables bulk create or delete. <br>This field must be true in order to delete with a filter rather than an identifier. |

## Example
```yaml
- name: Execute 'createMultipleNetmapVuln' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createMultipleNetmapVuln"
    data:
        id: "12345"
        type: "Vuln"
        ipAddress: "192.168.1.2"
        source: "MyVulnSource"
        cve: "2021-12345"
        description: "Description of the vuln"
        protocol: "tcp"
        port: 443
    path_params:
        domainUUID: "{{ domain_uuid }}"
    query_params:
        bulk: "{{ bulk }}"

```
