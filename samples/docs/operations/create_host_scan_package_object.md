# createHostScanPackageObject

The createHostScanPackageObject operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/hostscanpackages](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/hostscanpackages.md) path.&nbsp;
## Description
**Retrieves, update, deletes or creates the HostScan packages. If no ID is specified for a GET, retrieves list of all HostScan packages. _Check the response section for applicable examples (if any)._**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createHostScanPackageObject' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createHostScanPackageObject"
    path_params:
        domainUUID: "{{ domain_uuid }}"

```