# createDeploymentRequest

The createDeploymentRequest operation handles configuration related to [/api/fmc_config/v1/domain/{domainUUID}/deployment/deploymentrequests](/paths//api/fmc_config/v1/domain/{domain_uuid}/deployment/deploymentrequests.md) path.&nbsp;
## Description
**Creates a request for deploying configuration changes to devices. _Check the response section for applicable examples (if any)._**

## Data Parameters Example
| Parameter | Value | Description |
| --------- | -------- | -------- |
| type | DeploymentRequest | Type of the Request object. This value is always DeploymentRequest. |
| version | 1457566762351 | Integer indicating the version to which the deployment should be done. |
| forceDeploy | False | Boolean indicating the deployment is force deploy or not. Value set to true only if device is not out-of-date and user wants to force a deployment. This should not be used unless needed. Default is false. |
| ignoreWarning | True | Boolean indicating whether the warnings needs to be ignored during the prevalidation of deployment job. Default is false. |
| deviceList | ['d94f7ada-d141-11e5-acf3-c41f7e67fb1b'] | List of device UUIDs for which the deployment has to triggered. |
| deploymentNote | yournotescomehere | User provided job note with max of 512 characters |

## Path Parameters
| Parameter | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
| domainUUID | True | string | Domain UUID |

## Example
```yaml
- name: Execute 'createDeploymentRequest' operation
  cisco.fmcansible.fmc_configuration:
    operation: "createDeploymentRequest"
    data:
        type: "DeploymentRequest"
        version: "1457566762351"
        forceDeploy: False
        ignoreWarning: True
        deviceList: ['d94f7ada-d141-11e5-acf3-c41f7e67fb1b']
        deploymentNote: "yournotescomehere"
    path_params:
        domainUUID: "{{ domain_uuid }}"

```
