# createMultipleNetmapHost

The createMultipleNetmapHost operation handles configuration related to [/api/fmc_netmap/v1/domain/{domainUUID}/hosts](/paths//api/fmc_netmap/v1/domain/{domain_uuid}/hosts.md) path.&nbsp;
## Description
**Creates, deletes, or retrieves a host in the Network Map. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value | Description |
| --------- | -------- | ----------- |
| type | Host | Type associated with resource: Host |
| ipAddress | ['192.168.1.2'] | List of IPs of the host. At this point, when creating a host, only one IP is supported, but must still be in an array |
| macAddress | AA:BB:CC:DD:EE:FF | MAC of the host. This is the primary MAC of the host |

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
- name: Execute 'createMultipleNetmapHost' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createMultipleNetmapHost"
    data:
        type: "Host"
        ipAddress: ['192.168.1.2']
        macAddress: "AA:BB:CC:DD:EE:FF"
    path_params:
        domainUUID: "{{ domain_uuid }}"
    query_params:
        bulk: "{{ bulk }}"

```
