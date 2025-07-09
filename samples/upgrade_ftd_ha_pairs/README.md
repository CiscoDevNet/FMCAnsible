# FTD-HA-UPGRADE

Ansible Playbook to Upgrade Firewall Threat Defense in High Availability Mode and Managed by Firewall Management Center

## Before running the Ansbile Playbook-
1. Make sure the Upgrade Package is already downloaded in the FMC
2. Set FMC IP/FQDN, Username and Password in the `hosts.ini` file
3. Set the variables in `vars.yml`
4. Install the required Ansible Collection using the following command: `ansible-galaxy collection install cisco.fmcansible`

## Command to run the Ansible Playbook
```bash
ansible-playbook -i hosts.ini ftd-ha-upgrade.yml
```