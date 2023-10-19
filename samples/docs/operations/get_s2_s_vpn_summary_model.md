# getS2SVpnSummaryModel

The getS2SVpnSummaryModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/policy/s2svpnsummaries](/paths//api/fmc_config/v1/domain/{domain_uuid}/policy/s2svpnsummaries.md) path.&nbsp;
## Description
**Retrieves all the configured S2S VPN in the system , with short summary along with the health of the tunnels.**

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| filter | False | string <td colspan=3> The filter criteria for which the details have to be fetched.Following filter are supported.User can enter one or many filter device:{deviceId};name:{Topology name}:routeBased:{true|false} |
| offset | False | integer <td colspan=3> Index of first item to return. |
| limit | False | integer <td colspan=3> Number of items to return. |
| expanded | False | boolean <td colspan=3> If set to true, the GET response displays a list of objects with additional attributes. |

## Example
```yaml
- name: Execute 'getS2SVpnSummaryModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "getS2SVpnSummaryModel"
    path_params:
        domainUUID: "{{ domain_uuid }}"
    query_params:
        filter: "{{ filter }}"
        offset: "{{ offset }}"
        limit: "{{ limit }}"
        expanded: "{{ expanded }}"

```