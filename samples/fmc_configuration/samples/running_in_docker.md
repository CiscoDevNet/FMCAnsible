## Before using this ansible collection, you needed one available FMCv host and one or more FTDv devices

## Using the collection in Docker

Run next steps inside repository

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

You can define variables in file "samples/fmc_configuration/samples/vars.yml" otherwise the default values will be used.

* Access policy, allow traffic by default

Variables:

accesspolicy_name | default('AccessPolicy1')

[example](https://github.com/CiscoDevNet/FMCAnsible/blob/main/samples/fmc_configuration/samples/access_policy.yml)

```
ansible-playbook -i /etc/ansible/hosts playbooks/fmc_configuration/samples/access_policy.yml
```


* FTD device registration

Variables:

ftd_ip | default('1.1.1.1')

reg_key | default('cisco')

ftd_name | default('FTD1')

[example](https://github.com/CiscoDevNet/FMCAnsible/blob/main/samples/fmc_configuration/samples/device_registration.yml)

```
ansible-playbook -i /etc/ansible/hosts playbooks/fmc_configuration/samples/device_registration.yml
```
* Security zones

Variables:

securityzone1_name | default('secz1')

securityzone2_name | default('secz2')

[example](https://github.com/CiscoDevNet/FMCAnsible/blob/main/samples/fmc_configuration/security_zones.yml)

```
ansible-playbook -i /etc/ansible/hosts playbooks/fmc_configuration/security_zones.yml
```

* NAT

Variables:

nat_polycy_name | default('Test-NAT-Policys3')

[example](https://github.com/CiscoDevNet/FMCAnsible/blob/main/samples/fmc_configuration/nat.yml)

```
ansible-playbook -i /etc/ansible/hosts playbooks/fmc_configuration/nat.yml
```
