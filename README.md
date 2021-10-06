# FMC Ansible Modules

A collection of Ansible modules that automate configuration management 
and execution of operational tasks on Cisco Firepower Power Center (FMC) devices using FMC REST API.

_This file describes the development and testing aspects. In case you are looking for 
the user documentation, please check [FMC Ansible docs on DevNet](https://developer.cisco.com/site/ftd-ansible/)._

## Installation Guide

The project contains four Ansible modules:

* [`fmc_configuration.py`](library/fmc_configuration.py) - manages device configuration via REST API. The module configures virtual and physical devices by sending HTTPS calls formatted according to the REST API specification;
* [`fmc_file_download.py`](library/fmc_file_download.py) - downloads files from FMC devices via HTTPS protocol;
* [`fmc_file_upload.py`](library/fmc_file_upload.py) - uploads files to FMC devices via HTTPS protocol;
* [`fmc_install.py`](library/fmc_install.py) - installs FMC images on hardware devices. The module performs a complete reimage of the Firepower system by downloading the new software image and installing it. 

Sample playbooks are located in the [`samples`](./samples) folder.

### Running playbooks in Docker

1. Build the default Docker image:
    ```
    docker build -t ftd-ansible .
    ```
    **NOTE** The default image is based on the release v0.1.0 of the [`FMCAnsible`](https://github.com/CiscoDevNet/FMCAnsible) and Python 3.6. 

2. You can build the custom Docker image:
    ```
    docker build -t fmc-ansible --build-arg PYTHON_VERSION=<2.7|3.5|3.6|3.7> --build-arg FMC_ANSIBLE_VERSION=<tag name | branch name> .
    ```

3. Create an inventory file that tells Ansible what devices to run the tasks on. [`sample_hosts`](./inventory/sample_hosts) shows an example of inventory file.

4. Run the playbook in Docker mounting playbook folder to `/ftd-ansible/playbooks` and inventory file to `/etc/ansible/hosts`:
    ```
    docker run -v $(pwd)/samples:/ftd-ansible/playbooks -v $(pwd)/inventory/sample_hosts:/etc/ansible/hosts ftd-ansible playbooks/network_object.yml
    ```

### Running playbooks locally 

1. Create a virtual environment and activate it:
```
virtualenv venv
. venv/bin/activate
```

2. Install dependencies:
`pip install -r requirements.txt`

3. Update Python path to include the project's directory:
```
export PYTHONPATH=.:$PYTHONPATH
```
  
4. Run the playbook:
``` 
ansible-playbook samples/network_object.yml
```

## Unit Tests

The project contains unit tests for Ansible modules, HTTP API plugin and util files. They can be found in `test/unit` directory. Ansible has many utils for mocking and running tests, so unit tests in this project also rely on them and including Ansible test module to the Python path is required.

### Running unit tests in Docker

1. Build the Docker image: 
```
docker build -t ftd-ansible-test test
```
By default, the Dockerfile clones `devel` branch of Ansible repository, but you can change it by adding
`--build-arg ANSIBLE_BRANCH=$BRANCH_NAME` to the build command.

2. Run unit tests with:
```
docker run -v $(pwd):/ftd-ansible ftd-ansible-test pytest test/
```
To run a single test, specify the filename at the end of command:
```
docker run -v $(pwd):/ftd-ansible ftd-ansible-test pytest test/unit/test_fdm_configuration.py
```

#### Troubleshooting

```
import file mismatch:
imported module 'test.unit.module_utils.test_common' has this __file__ attribute: ...
which is not the same as the test file we want to collect:
  /ftd-ansible/test/unit/module_utils/test_common.py
HINT: remove __pycache__ / .pyc files and/or use a unique basename for your test file modules
```

In case you experience the following error while running the tests in Docker, remove compiled bytecode files files with 
`find . -name "*.pyc" -type f -delete` command and try again.

### Running unit tests locally

1. Clone [Ansible repository](https://github.com/ansible/ansible) from GitHub;
```
git clone https://github.com/ansible/ansible.git
```

**NOTE**: The next steps can be hosted in docker container
```
docker run -it -v `pwd`:/ftd-ansible python:3.6 bash
cd /ftd-ansible
pip download $(grep ^ansible ./requirements.txt) --no-cache-dir --no-deps -d /tmp/pip 
mkdir /tmp/ansible
tar -C /tmp/ansible -xf /tmp/pip/ansible*
mv /tmp/ansible/ansible* /ansible
rm -rf /tmp/pip /tmp/ansible
```

2. Install Ansible and test dependencies:
```
export ANSIBLE_DIR=`pwd`/ansible
pip install -r requirements.txt
pip install -r $ANSIBLE_DIR/requirements.txt
pip install -r test-requirements.txt
```

3. Add Ansible modules to the Python path:
```
export PYTHONPATH=$PYTHONPATH:$ANSIBLE_DIR/lib:$ANSIBLE_DIR/test
```

4. Run unit tests:
```
pytest tests/unit
```
 
### Running tests with [TOX](https://tox.readthedocs.io/en/latest/) 
**NOTE**: To be able to run tests with the specific version of Python using tox you need to have this version of Python installed locally  

Install tox locally:
```
pip install tox
```
Check the list of currently supported environments:
```
tox -l
```
**NOTE**: environments with _-integration_ postfix preconfigured for integration tests:

Setup `PYTHONPATH` as described in the previous section
Run unit tests in virtualenvs using tox:
```
tox -e py27,py35,py36,py37
```
Run integration tests in virtualenvs using tox:
```
export REPORTS_DIR=<path to the folder where JUnit reports will be stored>
tox -e py27-integration,py35-integration,py36-integration,py37-integration -- samples/network_object.yml -i inventory/sample_hosts
```
### Running style check locally
1. Install [Flake8](http://flake8.pycqa.org/en/latest/) locally:
    ```
    pip install flake8
    ```

2. Run Flake8 check:
    ```
    flake8
    ```

Flake8 configuration is defined in the [tox config file](./tox.ini) file.

## Integration Tests

Integration tests are written in a form of playbooks and usually started with `ansible-test` command from Ansible repository. As this project is created outside Ansible, it does not have utils to run the tests. Thus, integration tests are written as sample playbooks with assertion and can be found in the `samples` folder. They start with `test_` prefix and can be run as usual playbooks.

## Developing Locally With Docker

1. Setup docker environment

```
docker run -it -v $(pwd):/ftd-ansible \
python:3.6 bash
```

2. Change to working directory

`cd /ftd-ansible`

3. Clone [Ansible repository](https://github.com/ansible/ansible) from GitHub;
```
git clone https://github.com/ansible/ansible.git
```

**NOTE**: The next steps can be hosted in docker container
```
pip download $(grep ^ansible ./requirements.txt) --no-cache-dir --no-deps -d /tmp/pip 
mkdir /tmp/ansible
tar -C /tmp/ansible -xf /tmp/pip/ansible*
mv /tmp/ansible/ansible* /ansible
rm -rf /tmp/pip /tmp/ansible
```


4. Install Ansible and test dependencies:

```
export ANSIBLE_DIR=`pwd`/ansible
pip install -r requirements.txt
pip install -r $ANSIBLE_DIR/requirements.txt
pip install -r test-requirements.txt
```

5. Add Ansible modules to the Python path:

```
export PYTHONPATH=$PYTHONPATH:.:$ANSIBLE_DIR/lib:$ANSIBLE_DIR/test
```

6. Run unit tests:
```
pytest ansible_collections/cisco/ftdansible/tests
```

7. Create an inventory file that tells Ansible what devices to run the tasks on. [`sample_hosts`](./inventory/sample_hosts) shows an example of inventory file.

8. Run an integration playbook.

```    
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/access_policy.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/access_rule_with_applications.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/access_rule_with_intrusion_and_file_policies.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/access_rule_with_logging.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/access_rule_with_networks.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/access_rule_with_urls.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/access_rule_with_users.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/anyconnect_package_file.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/backup.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/data_dns_settings.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/deployment.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/dhcp_container.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/download_upload.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/ha_join.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/identity_policy.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/initial_provisioning.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/nat.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/network_object_with_host_vars.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/network_object.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/physical_interface.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/port_object.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/ra_vpn_license.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/ra_vpn.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/security_intelligence_url_policy.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/smart_license.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/ssl_policy.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/static_route_entry.yml
ansible-playbook -i inventory/sample_hosts samples/ftd_configuration/sub_interface.yml
```

## Debugging

1. Add `log_path` with path to log file in `ansible.cfg`

2. Run `ansible-playbook` with `-vvvv`
    ```
    $ ansible-playbook samples/network_object.yml -vvvv
    ```

3. The log file will contain additional information (REST, etc.)
