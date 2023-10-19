# createAnyConnectCustomAttributeModel

The createAnyConnectCustomAttributeModel operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/anyconnectcustomattributes](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/anyconnectcustomattributes.md) path.&nbsp;
## Description
**Retrieves the AnyConnect Custom Attribute associated with the specified ID. If no ID is specified for a GET, retrieves list of all AnyConnect Custom Attribute objects. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| attributeType | DYNAMIC_SPLIT_TUNNELING |
| type | AnyConnectCustomAttribute |
| dynamicSplitTunnel | {'includeDomains': ['cisco1.com', 'cisco2.com'], 'excludeDomains': ['cisco3.com', 'cisco4.com']} |
| overridable | False |
| description | Dynamic Split Tunneling rest |
| name | AnyConnectCustAttr_DynamicSplitTunnel1 |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'createAnyConnectCustomAttributeModel' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createAnyConnectCustomAttributeModel"
    data:
        attributeType: DYNAMIC_SPLIT_TUNNELING
        type: AnyConnectCustomAttribute
        dynamicSplitTunnel: {'includeDomains': ['cisco1.com', 'cisco2.com'], 'excludeDomains': ['cisco3.com', 'cisco4.com']}
        overridable: False
        description: Dynamic Split Tunneling rest
        name: AnyConnectCustAttr_DynamicSplitTunnel1
    path_params:
        domainUUID: "{{ domain_uuid }}"

```