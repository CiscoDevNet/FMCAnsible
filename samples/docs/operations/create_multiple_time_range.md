# createMultipleTimeRange

The createMultipleTimeRange operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/timeranges](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/timeranges.md) path.&nbsp;
## Description
**Retrieves, deletes, creates and modifies the TimeRange object. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value | Description |
| --------- | -------- | -------- |
| name | TestTimeRange | User assigned resource name. |
| effectiveStartDateTime | 2019-09-19T15:53:00 | Represents the absolute date and time (in ISO 8601 format) at which the time range object starts being effective. If not specified, value is considered, 'starts now'. |
| effectiveEndDateTime | 2019-09-21T17:53:00 | Represents the absolute date and time (in ISO 8601 format) at which the time range object stops being effective. If not specified, value is considered, 'never ends'. |
| recurrenceList | [{'recurrenceType': 'DAILY_INTERVAL', 'days': ['MON', 'TUE', 'FRI'], 'dailyStartTime': '08:00', 'dailyEndTime': '09:00'}, {'recurrenceType': 'RANGE', 'rangeStartTime': '09:00', 'rangeStartDay': 'MON', 'rangeEndTime': '11:00', 'rangeEndDay': 'FRI'}] | Represents the list of recurring intervals during which the time range is effective. These intervals are valid only between effectiveStartDateTime and effectiveEndDateTime. |
| type | TimeRange | Type of the response object. This value is always TimeRange. |
| description |   | User provided resource description. |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string | Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| bulk | False | boolean | Enables bulk create for TimeRange objects. |

## Example
```yaml
- name: Execute 'createMultipleTimeRange' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createMultipleTimeRange"
    data:
        name: "TestTimeRange"
        effectiveStartDateTime: "2019-09-19T15:53:00"
        effectiveEndDateTime: "2019-09-21T17:53:00"
        recurrenceList: [{'recurrenceType': 'DAILY_INTERVAL', 'days': ['MON', 'TUE', 'FRI'], 'dailyStartTime': '08:00', 'dailyEndTime': '09:00'}, {'recurrenceType': 'RANGE', 'rangeStartTime': '09:00', 'rangeStartDay': 'MON', 'rangeEndTime': '11:00', 'rangeEndDay': 'FRI'}]
        type: "TimeRange"
        description: " "
    path_params:
        domainUUID: "{{ domain_uuid }}"
    query_params:
        bulk: "{{ bulk }}"

```
