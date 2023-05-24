## Before using this ansible collection, you needed one available FMCv host and one or more FTDv devices

## Using the collection in Docker

1. Setup docker environment

```
docker run -it -v $(pwd)/samples:/fmc-ansible/playbooks \
-v $(pwd)/ansible.cfg:/fmc-ansible/ansible.cfg \
-v $(pwd)/requirements.txt:/fmc-ansible/requirements.txt \
-v $(pwd)/inventory/sample_hosts:/etc/ansible/hosts \
python:3.10 bash

cd /fmc-ansible
pip install -r requirements.txt
```

2. Install the ansible collection

```
ansible-galaxy collection install git+https://github.com/CiscoDevNet/FMCAnsible.git
```

3. List installed collections.
```
ansible-galaxy collection list
```

3. Validate your ansible.cfg file contains a path to ansible collections:

```
cat ansible.cfg
```
4. Edit hosts file `inventory/sample_hosts`  and add your FMC device IP address/credentials.

5. Reference the collection from your playbook

**NOTE**: The tasks in the playbook reference the collection

```
- hosts: all
  connection: httpapi
  tasks:
    - name: Find a Google application
      cisco.fmcansible.fmc_configuration:
        operation: getApplicationList
        filters:
          name: Google
        register_as: google_app_results
```        

Run the sample playbook.

```
ansible-playbook -i /etc/ansible/hosts playbooks/fmc_configuration/access_policy.yml
ansible-playbook -i /etc/ansible/hosts playbooks/fmc_configuration/nat.yml
```

All playbooks:

You can define variables in file "samples/fmc_configuration/vars.yml" otherwise the default values will be used.

* Access policy, allow traffic by default

[example](https://github.com/CiscoDevNet/FMCAnsible/blob/main/samples/fmc_configuration/access_policy.yml)

```
ansible-playbook -i /etc/ansible/hosts playbooks/fmc_configuration/access_policy.yml
```

* Access rule with networks

Variables:

networkobject_name | default('ansible-test-network466')

networkobject_ip | default('192.22.22.0/24')

accesspolicy_name | default('NGFW-Access-Policy25')

[example](https://github.com/CiscoDevNet/FMCAnsible/blob/main/samples/fmc_configuration/access_rule_with_networks.yml)

```
ansible-playbook -i /etc/ansible/hosts playbooks/fmc_configuration/access_rule_with_networks.yml
```

* Create an access rule logging malware files

[example](https://github.com/CiscoDevNet/FMCAnsible/blob/main/samples/fmc_configuration/access_rule_with_logging.yml)

```
ansible-playbook -i /etc/ansible/hosts playbooks/fmc_configuration/access_rule_with_logging.yml
```

* Data dns settings, create custom DNS object

Variables:

dnsserevergroup_name | default('CustomDNSServerGroup')

dnsserver1_ip | default('1.2.3.4')

dnsserver2_ip | default('2.2.3.4')

[example](https://github.com/CiscoDevNet/FMCAnsible/blob/main/samples/fmc_configuration/data_dns_settings.yml)

```
ansible-playbook -i /etc/ansible/hosts playbooks/fmc_configuration/data_dns_settings.yml
```

* FTD device registration

Variables:

ftd_ip | default('1.1.1.1')

reg_key | default('cisco')

ftd_name | default('FTD1')

[example](https://github.com/CiscoDevNet/FMCAnsible/blob/main/samples/fmc_configuration/device_registration.yml)

```
ansible-playbook -i /etc/ansible/hosts playbooks/fmc_configuration/device_registration.yml
```

* Dns server group

Variables:

dnsserevergroup_name | default('CustomDNSServerGroup')

dnsserver1_ip | default('1.2.3.4')

dnsserver2_ip | default('2.2.3.4')

[example](https://github.com/CiscoDevNet/FMCAnsible/blob/main/samples/fmc_configuration/dnsservergroup.yml)

```
ansible-playbook -i /etc/ansible/hosts playbooks/fmc_configuration/dnsservergroup.yml
```

* NAT

Variables:

nat_polycy_name | default('Test-NAT-Policys3')

[example](https://github.com/CiscoDevNet/FMCAnsible/blob/main/samples/fmc_configuration/nat.yml)

```
ansible-playbook -i /etc/ansible/hosts playbooks/fmc_configuration/nat.yml
```

* Network object

Variables:

networkobject_ftd1_name | default('net-15')

networkobject_ftd2_value | default('10.10.30.0/24')

networkobject_ftd1_name | default('net-13')

networkobject_ftd2_value | default('10.10.40.0/24')

networkgroup_name | default('netg-1')

[example](https://github.com/CiscoDevNet/FMCAnsible/blob/main/samples/fmc_configuration/network_object.yml)

```
ansible-playbook -i /etc/ansible/hosts playbooks/fmc_configuration/network_object.yml
```

* Physical interface

Variables:

outside_ip | default('192.168.10.4')

outside_netmask | default('255.255.255.0')

inside_ip | default('192.168.20.2')

inside_netmask | default('255.255.255.0')

[example](https://github.com/CiscoDevNet/FMCAnsible/blob/main/samples/fmc_configuration/physical_interface.yml)

```
ansible-playbook -i /etc/ansible/hosts playbooks/fmc_configuration/physical_interface.yml
```

* Port object

[example](https://github.com/CiscoDevNet/FMCAnsible/blob/main/samples/fmc_configuration/port_object.yml)

```
ansible-playbook -i /etc/ansible/hosts playbooks/fmc_configuration/port_object.yml
```

* Prefilter policy

Variables:

prefilterpolicy_name | default('NGFW-Prefilter-Policy104')

[example](https://github.com/CiscoDevNet/FMCAnsible/blob/main/samples/fmc_configuration/prefilter_policy.yml)

```
ansible-playbook -i /etc/ansible/hosts playbooks/fmc_configuration/prefilter_policy.yml
```

* Prefilter rule

[example](https://github.com/CiscoDevNet/FMCAnsible/blob/main/samples/fmc_configuration/prefilter_rule.yml)

```
ansible-playbook -i /etc/ansible/hosts playbooks/fmc_configuration/prefilter_rule.yml
```

* Security zones

[example](https://github.com/CiscoDevNet/FMCAnsible/blob/main/samples/fmc_configuration/security_zones.yml)

```
ansible-playbook -i /etc/ansible/hosts playbooks/fmc_configuration/security_zones.yml
```

* Static route

Variables:

firstdestinationnetwork | default('192.168.4.0/24')

seconddestinationnetwork | default('192.168.6.0/24')

gatewaynetwork | default('192.168.2.2')

[example](https://github.com/CiscoDevNet/FMCAnsible/blob/main/samples/fmc_configuration/static_route.yml)

```
ansible-playbook -i /etc/ansible/hosts playbooks/fmc_configuration/static_route.yml
```

* Sub interfaces

Variables:

subinterface_ip | default('192.168.5.15')

subinterface_ip | default('192.168.5.15')

[example](https://github.com/CiscoDevNet/FMCAnsible/blob/main/samples/fmc_configuration/sub_interfaces.yml)

```
ansible-playbook -i /etc/ansible/hosts playbooks/fmc_configuration/sub_interfaces.yml
```


## Tests

The project contains unit tests for Ansible modules, HTTP API plugin and util files. They can be found in `test/unit` directory. Ansible has many utils for mocking and running tests, so unit tests in this project also rely on them and including Ansible test module to the Python path is required.

### Running Sanity Tests Using Docker

When running sanity tests locally this project needs to be located at a path under ansible_collections/cisco (for example ansible_collections/cisco/fmcansible).  

```
rm -rf tests/output
ansible-test sanity --docker -v --color
```

### Running Units Tests Using Docker

When running sanity tests locally this project needs to be located at a path under ansible_collections/cisco (for example ansible_collections/cisco/fmcansible)


```
rm -rf tests/output
ansible-test units --docker -v --color
```

To run a single test, specify the filename at the end of command:
```
rm -rf tests/output
ansible-test units --docker -v tests/unit/httpapi_plugins/test_ftd.py --color
```

### Integration Tests

Integration tests are written in a form of playbooks. Thus, integration tests are written as sample playbooks with assertion and can be found in the `samples` folder. They can be run as usual playbooks.  The integration tests use a local Docker container which copies the necessary code and folders from your local path into a docker container for testing.

1. Build the default Python 3.9, Ansible 2.10 Docker image:
    ```
    docker build -t fmc-ansible:integration -f Dockerfile_integration .
    ```
    **NOTE**: The default image is based on the release v0.1.0 of the [`FMC-Ansible`](https://github.com/CiscoDevNet/FMCAnsible) and Python 3.6.

2. You can build the custom Docker image:
    ```
    docker build -t fmc-ansible:integration \
    -f Dockerfile_integration \
    --build-arg PYTHON_VERSION=<2.7|3.5|3.6|3.7> \
    --build-arg FMC_ANSIBLE_VERSION=<tag name | branch name> .
    ```

3. Create an inventory file that tells Ansible what devices to run the tasks on. [`sample_hosts`](./inventory/sample_hosts) shows an example of inventory file.

4. Run the playbook in Docker mounting playbook folder to `/fmc-ansible/playbooks` and inventory file to `/etc/ansible/hosts`:

    ```
    docker run -v $(pwd)/inventory/sample_hosts:/etc/ansible/hosts \
    -v $(pwd)/ansible.cfg:/root/ansible_collections/cisco/fmcansible/ansible.cfg \
    fmc-ansible:integration /root/ansible_collections/cisco/fmcansible/samples/fmc_configuration/latest.yml
    ```
IMPORTANT: When cloning this repository place it under ansible_collections/cisco (requirement to run some of the Ansible tools like ansible-test).

## Developing Locally With Docker

1. Setup docker environment

```
docker run -it -v $(pwd):/root/ansible_collections/cisco/fmcansible \
python:3.10 bash
```

2. Change to working directory, update and upgrade system and install requirements.txt

```
cd /root/ansible_collections/cisco/fmcansible
apt update && apt upgrade -y
pip install -r requirements.txt
```

3. Create an inventory file that tells Ansible what devices to run the tasks on. [`sample_hosts`](./inventory/sample_hosts) shows an example of inventory file.


## Debugging

1. Add `log_path` with path to log file in `ansible.cfg`

2. Run `ansible-playbook` with `-vvvv`
    ```
    $ ansible-playbook -i inventory/sample_hosts samples/fmc_configuration/access_policy.yml -vvvv
    ```

3. The log file will contain additional information (REST, etc.)
