# Cisco Secure Firewall Management Center (FMC) Ansible Collection

An Ansible Collection that automates configuration management 
and execution of operational tasks on Cisco Secure Firewall Management Centre (FMC) devices using FMC REST API. This module is essentially a wrapper to take an Ansible playbook and converts each play into an FMC API call. The advantage of this is that it does not need to be updated with new versions of FMC. A downside to this approach is that the playbooks do not have the traditional Ansible look and feel.
We are planning to build templates and roles to try and make the Ansible playbooks more feel like typical Ansible and easier to learn and use.


This module has been tested against the following cisco Secure Firewall Management Center versions up to 7.6

## Included Content

The collection contains one Ansible module:

* [`fmc_configuration.py`](https://github.com/CiscoDevNet/FMCAnsible/blob/main/plugins/modules/fmc_configuration.py) - manages device configuration via REST API. The module configures virtual and physical devices by sending HTTPS calls formatted according to the REST API specification.

## Installing this collection

You can install the Cisco DCNM collection with the Ansible Galaxy CLI:

```
ansible-galaxy collection install cisco.fmcansible
```

## Usage Instruction

Create the inventory file. Ansible inventory contains information about systems where the playbooks should be run. You should create an inventory file with information about the FMC that will be used for configuration.

The default location for inventory is /etc/ansible/hosts, but you can specify a different path by adding the `-i <path>` argument to the ansible-playbook command.

The inventory file requires:

-       Hostname or IP Address of the FMC

-       Username for FMC

-       Password for the given user

```
[all:vars]
ansible_network_os=cisco.fmcansible.fmc

[vfmc]
<FMC IP> ansible_user=<username> ansible_password=<password> ansible_httpapi_port=443 ansible_httpapi_use_ssl=True ansible_httpapi_validate_certs=True
```

Then create a playbook referencing the module and the desired operation. This example `network.yml` demonstrates how to create a simple network object. The task creates a new object representing the subnet.

After creation, the network object is stored as an Ansible fact and can be accessed  
using `Network_net15` variable.

```ansible
- hosts: all
  connection: httpapi
  tasks:
    - name: Get Domain UUID
      cisco.fmcansible.fmc_configuration:
        operation: getAllDomain
        register_as: domain

    - name: Create a network object for Cisco FTD 1
      cisco.fmcansible.fmc_configuration:
        operation: createMultipleNetworkObject
        data:
          name: net15
          value: 10.10.30.0/24
          type: Network
        path_params:
          domainUUID: '{{ domain[0].uuid }}'
```
Then run the playbook

```
ansible-playbook -i hosts network.yml
```

Detailed Usage Instructions can be found [here](https://github.com/CiscoDevNet/FMCAnsible/blob/main/docs/usage.md)


Sample playbooks are located [`here`](https://github.com/CiscoDevNet/FMCAnsible/tree/main/samples).

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [Cisco FMCAnsible repository](https://github.com/CiscoDevNet/FMCAnsible)

