# deleteHostScanPackageObject

The deleteHostScanPackageObject operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/hostscanpackages/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/hostscanpackages/{object_id}.md) path.&nbsp;
## Description
**Retrieves, update, deletes or creates the HostScan packages. If no ID is specified for a GET, retrieves list of all HostScan packages. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Identifier for HostScan packages. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'deleteHostScanPackageObject' operation
  cisco.fmcansible.fmc_configuration:
    operation: "deleteHostScanPackageObject"
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```