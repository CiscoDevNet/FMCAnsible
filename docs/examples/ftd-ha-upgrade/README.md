# FTD HA Upgrade - Role-based Implementation

This directory contains a role-based implementation of the FTD HA upgrade process using Cisco FMC Ansible collection. This approach breaks down the complex upgrade process into reusable, modular roles.

## Overview

The FTD HA upgrade process has been decomposed into the following roles:

1. **get_domains** - Retrieves FMC domains
2. **get_upgrade_packages** - Retrieves and filters upgrade packages by version
3. **get_ha_devices** - Retrieves HA device containers and builds target lists
4. **device_backup** - Creates and monitors device backups
5. **device_upgrade** - Performs readiness checks and upgrades

## Prerequisites

1. Ansible 2.10 or higher
2. cisco.fmcansible collection installed:
   ```bash
   ansible-galaxy collection install cisco.fmcansible
   ```
3. FMC with HA devices configured
4. Upgrade package already downloaded to the FMC

## Configuration

### 1. Update Inventory File

Edit `hosts.ini` with your FMC details:
```ini
[fmc]
your-fmc-ip ansible_user=admin ansible_password=password ansible_network_os=cisco.fmcansible.fmc ansible_httpapi_port=443 ansible_httpapi_use_ssl=yes ansible_httpapi_validate_certs=no
```

### 2. Update Variables

Edit `vars.yml` with your environment specifics:
```yaml
---
version: "7.7.0-89"  # Version string to filter upgrade packages
ha_pair_names: 
  - "HA-Pair-1"
  - "HA-Pair-2"  # Add more HA pairs as needed

# Optional: Output directory for saving task results and logs
output_directory: "./ftd_upgrade_logs"
```

## Usage

Run the upgrade playbook:
```bash
ansible-playbook -i hosts.ini ftd-ha-upgrade.yml
```

## Role Features

### Modular Design
Each role can be used independently or as part of the complete upgrade workflow:

```yaml
# Use individual roles in your own playbooks
- role: get_upgrade_packages
  vars:
    version_filter: "7.7.0"
    filter_by_version: true

```yaml
# Just perform backup
- role: device_backup
  vars:
    domain_uuid: "{{ ansible_facts['fmc_domains'][0].uuid }}"
    target_devices: "{{ ansible_facts['ha_devices_target_containers'] }}"
    wait_for_completion: true
```
```

### Flexible Configuration
Roles support extensive customization through variables:

- **Retry logic**: Configurable retries and delays for long-running tasks
- **Output options**: Save task results to JSON files for audit trails
- **Filtering**: Filter devices and packages by various criteria
- **Monitoring**: Optional task completion monitoring with verification

### Error Handling
- Comprehensive validation of required variables
- Graceful failure handling with meaningful error messages
- Task status monitoring with configurable timeouts

## Workflow Steps

1. **Domain Discovery**: Identifies the FMC domain to work with
2. **Package Selection**: Finds and filters upgrade packages by version
3. **Device Discovery**: Locates HA device pairs and prepares target lists
4. **Backup Creation**: Creates device backups with completion monitoring
5. **Readiness Check**: Validates devices are ready for upgrade
6. **Upgrade Execution**: Performs the actual upgrade with monitoring

## Output Files

When `save_to_file` is enabled, each role generates JSON output files:

- `fmc_domains.json` - Domain information
- `upgrade_packages.json` - Available upgrade packages
- `ha_devices.json` - HA device container details
- `backup_task.json` - Backup task information
- `readiness_check_task.json` - Readiness check results
- `upgrade_task.json` - Upgrade task details

## Benefits over Original Sample

1. **Reusability**: Individual roles can be used in other playbooks
2. **Maintainability**: Smaller, focused components are easier to maintain
3. **Flexibility**: Each role can be configured independently
4. **Testing**: Individual components can be tested in isolation
5. **Documentation**: Each role includes comprehensive documentation
6. **Error Handling**: Improved error messages and validation
7. **Monitoring**: Better task monitoring and status reporting

## Troubleshooting

1. **Connection Issues**: Verify FMC credentials and network connectivity
2. **Package Not Found**: Ensure the version filter matches available packages
3. **HA Pair Not Found**: Verify HA pair names match exactly in FMC
4. **Timeout Issues**: Increase retry counts and delays for slower environments

## Advanced Usage

### Using Individual Roles

```yaml
# Just get upgrade packages
- role: get_upgrade_packages
  vars:
    register_as: my_packages
    save_to_file: true

# Just perform backup
- role: device_backup
  vars:
    domain_uuid: "{{ domain_id }}"
    target_devices: "{{ my_target_list }}"
    wait_for_completion: true
```

### Custom Error Handling

```yaml
- role: device_upgrade
  vars:
    verify_success: false  # Handle errors manually
  ignore_errors: true

- name: Custom error handling
  debug:
    msg: "Upgrade failed, but continuing with rollback..."
  when: ansible_facts['device_upgrade_status'].status == "FAILED"
```

This role-based approach provides a more maintainable and flexible solution for FTD HA upgrades while preserving all the functionality of the original monolithic playbook.
