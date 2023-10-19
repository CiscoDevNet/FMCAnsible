# createInternalCA

The createInternalCA operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/object/internalcas](/paths//api/fmc_config/v1/domain/{domain_uuid}/object/internalcas.md) path.&nbsp;
## Description
**Retrieves, deletes, creates, or modifies the Internal CA associated with the specified ID. If no ID is specified, retrieves list of all Internal CAs. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value |
| --------- | -------- |
| name | import_CA_2 |
| cert | -----BEGIN CERTIFICATE-----
MIIDYDCCAsmgAwIBAgIJAPqlXa5mNBMXMA0GCSqGSIb3DQEBBQUAMH4xCzAJBgNV
BAYTAlVTMQswCQYDVQQIEwJQQTETMBEGA1UEBxMKUGl0dHNidXJnaDETMBEGA1UE
ChMKU291cmNlZmlyZTEiMCAGA1UEAxMZaW50ZXJuYWwxMDI0LmludGVybmFsMTAy
NDEUMBIGA1UECxMLRGV2ZWxvcG1lbnQwHhcNMTUwMzEwMTU0NTUxWhcNMjUwMzA3
MTU0NTUxWjB+MQswCQYDVQQGEwJVUzELMAkGA1UECBMCUEExEzARBgNVBAcTClBp
dHRzYnVyZ2gxEzARBgNVBAoTClNvdXJjZWZpcmUxIjAgBgNVBAMTGWludGVybmFs
MTAyNC5pbnRlcm5hbDEwMjQxFDASBgNVBAsTC0RldmVsb3BtZW50MIGfMA0GCSqG
SIb3DQEBAQUAA4GNADCBiQKBgQCivQIImKK+11/BUxESTfgy/F1bYkM+NapK8jOg
x9DF1y+5wDBqaoFpNzCCEgC3I/NfehI+KbuJFwgO7i4+IGqRkDZtNxmQ8SsEwEQ6
imwl+brHNFcXLrw/Ih5OW9JuSgU1Zc2bx2O7CAFLMuuJxFtyFImFwf+X2f8namOt
8FPKFQIDAQABo4HlMIHiMAwGA1UdEwQFMAMBAf8wHQYDVR0OBBYEFO6c6Fbf5jtC
sDJ4RsCip+KcZM46MIGyBgNVHSMEgaowgaeAFO6c6Fbf5jtCsDJ4RsCip+KcZM46
oYGDpIGAMH4xCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJQQTETMBEGA1UEBxMKUGl0
dHNidXJnaDETMBEGA1UEChMKU291cmNlZmlyZTEiMCAGA1UEAxMZaW50ZXJuYWwx
MDI0LmludGVybmFsMTAyNDEUMBIGA1UECxMLRGV2ZWxvcG1lbnSCCQD6pV2uZjQT
FzANBgkqhkiG9w0BAQUFAAOBgQBL8xwr1cijq0pAS4DlgLF2hT1Q+rP6/qpW6sp3
hGgtdyk6jC/UofWERS6Y5YYkrEfTLJltXRK6ndBKgwpisBY3krwIFGY0kIyxgEko
42/r3JM6GJZEfRfurXVazELShfjI8WFolnJawBU6Bvt8opY4BHkdyBChNWcYZsLu
rIuPFw==
-----END CERTIFICATE----- |
| privateKey | -----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,D551E502980434E1D94D52679CD5366D

NnvhG2o/0czQ8P6HIRVB8NBEhDpWlkt5Dt9VwlHvDd4PUaFOz//mF6F/JHOO/7Tw
9/hrzKUoL/KMz2guer903CxnVCr4tpHiAOpXKe/jxcoXW8T6NdMBe2sfdkzRfmoJ
YsjjhFAY20TlEt1/uhpdISPCjNo4p3dQwDGFaNQn9KyPZdsxVEWWtTvBoXtSE4xp
zY8wVJzUsmZTexGnu6OUC+i46UdcrHFIZTiRQLNDcYTIRU3A3bTMi88HuJJIA7Ig
OJ1fKEPvtMpibsSsw9X/+1suIWdR1HnLWvUGjPjObYLezsz0+kbyc+/fJVT/QM5a
Lvwitna48hffVKHrQl2g8d8rWo1mPnNKMGf0UyBdGw2h+00pdi6fIhuoDYDQM6UK
MHJBt/cX6+p0qfhzi/67NenkHgO5WAkNfSpRnVXfnWVc3Q0Cgv1vC/mAnoepxMMV
8yjmABpgSpG8Y3Itb4XC+yhejxhhDdxzWuxuGBN/XcsGmrb6dYxqhWwAZ3QNJoVQ
ZQtRDJQsA6YwOEFjvjBGZBwrOxVXRd/vPwq1bIN2rE6DCj8AQQk1GkjV/gs6U2cB
7PUnKj0Zh/bbs5e9VF4irb9+Tj7GAeKhytqiBWvbjYPbit21alSFqHsnoEBJBzMT
2Qhiy+/J1HkQOlPG5aczCxLrjUfe9BOxvjD31T+kfmOqBsdgamH0LhK8yXl1vn0f
Z0rcQw3ADuxLT0qZ1zveJTaAEp7bJrIC+mnvCjuKJ8tPjgWqtfC797SwFNi7g49G
BimfKqNhNJahbgUyRxVmgtzPydzBcZ23pQfI/+Yg4eIFcwxRXo6vcWEb3S3sg0PY
-----END RSA PRIVATE KEY----- |
| passPhrase | password |
| subjectCountry | US |
| type | InternalCA |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string <td colspan=3> Domain UUID |

## Query Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| isCSR | False | boolean <td colspan=3> Boolean parameter to specify if the request is to create a Certificate Signing Request(CSR) or not. <code>false</code> by default. When <code>false</code>, if a certificate/key pair is provided, the certificate/key pair is imported. Else, a self-signed certificate is generated. When <code>true</code>, a CSR is generated. |

## Example
```yaml
- name: Execute 'createInternalCA' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createInternalCA"
    data:
        name: import_CA_2
        cert: -----BEGIN CERTIFICATE-----
MIIDYDCCAsmgAwIBAgIJAPqlXa5mNBMXMA0GCSqGSIb3DQEBBQUAMH4xCzAJBgNV
BAYTAlVTMQswCQYDVQQIEwJQQTETMBEGA1UEBxMKUGl0dHNidXJnaDETMBEGA1UE
ChMKU291cmNlZmlyZTEiMCAGA1UEAxMZaW50ZXJuYWwxMDI0LmludGVybmFsMTAy
NDEUMBIGA1UECxMLRGV2ZWxvcG1lbnQwHhcNMTUwMzEwMTU0NTUxWhcNMjUwMzA3
MTU0NTUxWjB+MQswCQYDVQQGEwJVUzELMAkGA1UECBMCUEExEzARBgNVBAcTClBp
dHRzYnVyZ2gxEzARBgNVBAoTClNvdXJjZWZpcmUxIjAgBgNVBAMTGWludGVybmFs
MTAyNC5pbnRlcm5hbDEwMjQxFDASBgNVBAsTC0RldmVsb3BtZW50MIGfMA0GCSqG
SIb3DQEBAQUAA4GNADCBiQKBgQCivQIImKK+11/BUxESTfgy/F1bYkM+NapK8jOg
x9DF1y+5wDBqaoFpNzCCEgC3I/NfehI+KbuJFwgO7i4+IGqRkDZtNxmQ8SsEwEQ6
imwl+brHNFcXLrw/Ih5OW9JuSgU1Zc2bx2O7CAFLMuuJxFtyFImFwf+X2f8namOt
8FPKFQIDAQABo4HlMIHiMAwGA1UdEwQFMAMBAf8wHQYDVR0OBBYEFO6c6Fbf5jtC
sDJ4RsCip+KcZM46MIGyBgNVHSMEgaowgaeAFO6c6Fbf5jtCsDJ4RsCip+KcZM46
oYGDpIGAMH4xCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJQQTETMBEGA1UEBxMKUGl0
dHNidXJnaDETMBEGA1UEChMKU291cmNlZmlyZTEiMCAGA1UEAxMZaW50ZXJuYWwx
MDI0LmludGVybmFsMTAyNDEUMBIGA1UECxMLRGV2ZWxvcG1lbnSCCQD6pV2uZjQT
FzANBgkqhkiG9w0BAQUFAAOBgQBL8xwr1cijq0pAS4DlgLF2hT1Q+rP6/qpW6sp3
hGgtdyk6jC/UofWERS6Y5YYkrEfTLJltXRK6ndBKgwpisBY3krwIFGY0kIyxgEko
42/r3JM6GJZEfRfurXVazELShfjI8WFolnJawBU6Bvt8opY4BHkdyBChNWcYZsLu
rIuPFw==
-----END CERTIFICATE-----
        privateKey: -----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,D551E502980434E1D94D52679CD5366D

NnvhG2o/0czQ8P6HIRVB8NBEhDpWlkt5Dt9VwlHvDd4PUaFOz//mF6F/JHOO/7Tw
9/hrzKUoL/KMz2guer903CxnVCr4tpHiAOpXKe/jxcoXW8T6NdMBe2sfdkzRfmoJ
YsjjhFAY20TlEt1/uhpdISPCjNo4p3dQwDGFaNQn9KyPZdsxVEWWtTvBoXtSE4xp
zY8wVJzUsmZTexGnu6OUC+i46UdcrHFIZTiRQLNDcYTIRU3A3bTMi88HuJJIA7Ig
OJ1fKEPvtMpibsSsw9X/+1suIWdR1HnLWvUGjPjObYLezsz0+kbyc+/fJVT/QM5a
Lvwitna48hffVKHrQl2g8d8rWo1mPnNKMGf0UyBdGw2h+00pdi6fIhuoDYDQM6UK
MHJBt/cX6+p0qfhzi/67NenkHgO5WAkNfSpRnVXfnWVc3Q0Cgv1vC/mAnoepxMMV
8yjmABpgSpG8Y3Itb4XC+yhejxhhDdxzWuxuGBN/XcsGmrb6dYxqhWwAZ3QNJoVQ
ZQtRDJQsA6YwOEFjvjBGZBwrOxVXRd/vPwq1bIN2rE6DCj8AQQk1GkjV/gs6U2cB
7PUnKj0Zh/bbs5e9VF4irb9+Tj7GAeKhytqiBWvbjYPbit21alSFqHsnoEBJBzMT
2Qhiy+/J1HkQOlPG5aczCxLrjUfe9BOxvjD31T+kfmOqBsdgamH0LhK8yXl1vn0f
Z0rcQw3ADuxLT0qZ1zveJTaAEp7bJrIC+mnvCjuKJ8tPjgWqtfC797SwFNi7g49G
BimfKqNhNJahbgUyRxVmgtzPydzBcZ23pQfI/+Yg4eIFcwxRXo6vcWEb3S3sg0PY
-----END RSA PRIVATE KEY-----
        passPhrase: password
        subjectCountry: US
        type: InternalCA
    path_params:
        domainUUID: "{{ domain_uuid }}"
    query_params:
        isCSR: "{{ is_csr }}"

```