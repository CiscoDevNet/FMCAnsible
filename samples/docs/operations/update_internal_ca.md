# updateInternalCA

The updateInternalCA operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/internalcas/{objectId}](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/internalcas/{object_id}.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the Internal CA associated with the specified ID. If no ID is specified, retrieves list of all Internal CAs. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| id | 31cba922-9c1b-11ec-bbc8-d3a155c5f4d0 |
| name | csr_test1 |
| type | InternalCA |
| cert | -----BEGIN CERTIFICATE-----
MIIC3jCCAkcCAQEwDQYJKoZIhvcNAQEFBQAwfjELMAkGA1UEBhMCVVMxCzAJBgNV
BAgTAlBBMRMwEQYDVQQHEwpQaXR0c2J1cmdoMRMwEQYDVQQKEwpTb3VyY2VmaXJl
MSIwIAYDVQQDExlpbnRlcm5hbDEwMjQuaW50ZXJuYWwxMDI0MRQwEgYDVQQLEwtE
ZXZlbG9wbWVudDAeFw0yMjAzMDUwMDM0NThaFw0yMzAzMDUwMDM0NThaMG0xCzAJ
BgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMREwDwYDVQQHDAhNaWxwaXRh
czEOMAwGA1UECgwFQ2lzY28xDDAKBgNVBAsMA1NCRzEYMBYGA1UEAwwPaW50ZXJu
YWxDQS5jc3IxMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA8qIxHaiv
kJKCD+KKH219DBrnEKHnYOkwfztcwkOoLPQgJ9Rl4FoBoYVjkus9ZPAuPMeK/D7B
m8PqGmvcadH7DcjA6W+/2grs3t1PyrihNlHuIQIedAhQxFXbJSpaUJaoSKVL2FgL
ev5G7Hy2nZI1kfSvAxUFNUL46CtzWmqvJ+H1lRL/Z/arC8JdNOcbOE/LAhrR6c4y
0WXxRnlPsYaScREHTAfh7W13QrQ79ymxa61fyYnUwI3gXFqRGdN9z4jdbzLhpY5Q
DsySe5xytraBumlimFcO0nxVlkKeDq7Ky5X1+LPL/vUKcIMP/1N5ZnxN2mvIshpW
0a5rSJrZSrQ0mQIDAQABMA0GCSqGSIb3DQEBBQUAA4GBAAHUXBwgJ7xtMisgdSUR
VzDRyc5JdR5VkWOxmxTQ5Wbqbs/p+1xRo1PxPu6cQAyCsyfzlVdU1uLHSxvUyW3k
DR9Y5vQau5085hznD8ROvMFYPHCFq68L0d1dWuvQt1Mvy04OYbIvR/C6539+n393
OULqbcG8DIPBdeRt+IkEOIM/
-----END CERTIFICATE----- |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| objectId | True | string <td colspan=3> Unique identifier of an Internal CA. |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Example
```yaml
- name: Execute 'updateInternalCA' operation
  cisco.fmcansible.fmc_configuration:
    operation: "updateInternalCA"
    data:
        id: 31cba922-9c1b-11ec-bbc8-d3a155c5f4d0
        name: csr_test1
        type: InternalCA
        cert: -----BEGIN CERTIFICATE-----
MIIC3jCCAkcCAQEwDQYJKoZIhvcNAQEFBQAwfjELMAkGA1UEBhMCVVMxCzAJBgNV
BAgTAlBBMRMwEQYDVQQHEwpQaXR0c2J1cmdoMRMwEQYDVQQKEwpTb3VyY2VmaXJl
MSIwIAYDVQQDExlpbnRlcm5hbDEwMjQuaW50ZXJuYWwxMDI0MRQwEgYDVQQLEwtE
ZXZlbG9wbWVudDAeFw0yMjAzMDUwMDM0NThaFw0yMzAzMDUwMDM0NThaMG0xCzAJ
BgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMREwDwYDVQQHDAhNaWxwaXRh
czEOMAwGA1UECgwFQ2lzY28xDDAKBgNVBAsMA1NCRzEYMBYGA1UEAwwPaW50ZXJu
YWxDQS5jc3IxMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA8qIxHaiv
kJKCD+KKH219DBrnEKHnYOkwfztcwkOoLPQgJ9Rl4FoBoYVjkus9ZPAuPMeK/D7B
m8PqGmvcadH7DcjA6W+/2grs3t1PyrihNlHuIQIedAhQxFXbJSpaUJaoSKVL2FgL
ev5G7Hy2nZI1kfSvAxUFNUL46CtzWmqvJ+H1lRL/Z/arC8JdNOcbOE/LAhrR6c4y
0WXxRnlPsYaScREHTAfh7W13QrQ79ymxa61fyYnUwI3gXFqRGdN9z4jdbzLhpY5Q
DsySe5xytraBumlimFcO0nxVlkKeDq7Ky5X1+LPL/vUKcIMP/1N5ZnxN2mvIshpW
0a5rSJrZSrQ0mQIDAQABMA0GCSqGSIb3DQEBBQUAA4GBAAHUXBwgJ7xtMisgdSUR
VzDRyc5JdR5VkWOxmxTQ5Wbqbs/p+1xRo1PxPu6cQAyCsyfzlVdU1uLHSxvUyW3k
DR9Y5vQau5085hznD8ROvMFYPHCFq68L0d1dWuvQt1Mvy04OYbIvR/C6539+n393
OULqbcG8DIPBdeRt+IkEOIM/
-----END CERTIFICATE-----
    path_params:
        objectId: "{{ object_id }}"
        domainUUID: "{{ domain_uuid }}"

```