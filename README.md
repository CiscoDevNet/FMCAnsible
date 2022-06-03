# FMC Ansible Modules

IMPORTANT: This is a beta build. It is still being tested. Please use it for testing and provide feedback, do not use in production.

IMPORTANT: When cloning this repository place it under ansible_collections/cisco (requirement to run some of the Ansible tools like ansible-test).

An Ansible Collection that automates configuration management 
and execution of operational tasks on Cisco Firepower Management Console (FMC) devices using FMC REST API.  

## Installation Guide

The collection contains four Ansible modules:

* [`fmc_configuration.py`](./ansible_collections/plugins/modules/fmc_configuration.py) - manages device configuration via REST API. The module configures virtual and physical devices by sending HTTPS calls formatted according to the REST API specification;

Sample playbooks are located in the [`samples`](./samples) folder.

## View Collection Documentation

Usage Instructions are presnt in the Instructions folder


## Using the collection in Ansible

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
4. Edit hosts file `samples/fmc_configuration/hosts`  and add your FMC device IP address/credentials.
   
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

Integration tests are written in a form of playbooks. Thus, integration tests are written as sample playbooks with assertion and can be found in the `samples` folder. They start with `test_` prefix and can be run as usual playbooks.  The integration tests use a local Docker container which copies the necessary code and folders from your local path into a docker container for testing.

1. Build the default Python 3.9, Ansible 2.10 Docker image:
    ```
    docker build -t fmc-ansible:integration -f Dockerfile_integration .
    ```
    **NOTE**: The default image is based on the release v0.4.0 of the [`FMC-Ansible`](https://github.com/CiscoDevNet/FMCAnsible) and Python 3.6. 

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

    docker run -v $(pwd)/inventory/sample_hosts:/etc/ansible/hosts \
    -v $(pwd)/ansible.cfg:/root/ansible_collections/cisco/fmcansible/ansible.cfg \
    fmc-ansible:integration /root/ansible_collections/cisco/fmcansible/samples/fmc_configuration/user.yml

    ```


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


See section Above 

## Debugging

1. Add `log_path` with path to log file in `ansible.cfg`

2. Run `ansible-playbook` with `-vvvv`
    ```
    $ ansible-playbook -i inventory/sample_hosts samples/fmc_configuration/access_policy.yml -vvvv
    ```

3. The log file will contain additional information (REST, etc.)


## Troubleshooting

```
import file mismatch:
imported module 'test.unit.module_utils.test_common' has this __file__ attribute: ...
which is not the same as the test file we want to collect:
  /fmc-ansible/test/unit/module_utils/test_common.py
HINT: remove __pycache__ / .pyc files and/or use a unique basename for your test file modules
```

In case you experience the following error while running the tests in Docker, remove compiled bytecode files files with 
`find . -name "*.pyc" -type f -delete` command and try again.

