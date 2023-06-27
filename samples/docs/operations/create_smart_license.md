# createSmartLicense

The createSmartLicense operation handles configuration related to [/api/fmc_platform/v1/license/smartlicenses](/paths//api/fmc_platform/v1/license/smartlicenses.md) path.&nbsp;
## Description
**API operations on Smart Licenses including: retrieving registration status, requesting license registration, de-registering Smart Licenses and activating evaluation mode.  _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| type | SmartLicense |
| registrationType | REGISTER |
| token | X2M3YmJlY... |

## Example
```yaml
- name: Execute 'createSmartLicense' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createSmartLicense"
    data:
        type: SmartLicense
        registrationType: REGISTER
        token: X2M3YmJlY...

```