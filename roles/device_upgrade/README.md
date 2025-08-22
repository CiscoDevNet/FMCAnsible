# Device Upgrade Role

This Ansible role performs device upgrades and readiness checks in Cisco Firepower Management Center (FMC).

## Requirements

- Ansible 2.10 or higher
- cisco.fmcansible collection

## Role Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `domain_uuid` | UUID of the FMC domain to use | Required - no default |
| `upgrade_package` | Upgrade package object with id and name | Required - no default |
| `target_devices` | List of target devices for upgrade | Required - no default |
| `register_as` | Name to register the upgrade result as | `device_upgrade` |
| `readiness_check_only` | Whether to perform only readiness check | `false` |
| `enable_upgrade_revert` | Whether to enable upgrade revert option | `true` |
| `auto_upgrade_cancel` | Whether to enable auto upgrade cancel | `true` |
| `wait_for_completion` | Whether to wait for upgrade completion | `true` |
| `max_retries` | Maximum number of retries for status checks | `60` |
| `retry_delay` | Delay between status checks (seconds) | `60` |
| `verify_success` | Whether to verify upgrade completed successfully | `true` |
| `output_dir` | Directory where JSON output files will be saved | `.` (current directory) |
| `save_to_file` | Whether to save the upgrade task info to a file | `false` |

## Example Playbook

```yaml
- name: Upgrade FMC Devices
  hosts: fmc
  gather_facts: no
  connection: httpapi
  collections:
    - cisco.fmcansible
  
  roles:
    # Readiness check first
    - role: device_upgrade
      vars:
        domain_uuid: "{{ domain_id }}"
        upgrade_package:
          id: "package-uuid-1"
          name: "Cisco_FTD_Upgrade-7.7.0-89.sh"
        target_devices:
          - id: "device-uuid-1"
            type: "Device"
            name: "FTD-1"
        readiness_check_only: true
        register_as: readiness_check
        
    # Actual upgrade
    - role: device_upgrade
      vars:
        domain_uuid: "{{ domain_id }}"
        upgrade_package:
          id: "package-uuid-1"
          name: "Cisco_FTD_Upgrade-7.7.0-89.sh"
        target_devices:
          - id: "device-uuid-1"
            type: "Device"
            name: "FTD-1"
        readiness_check_only: false
        enable_upgrade_revert: true
        auto_upgrade_cancel: true
        register_as: device_upgrade
```

## Return Values

The role sets the following facts:

- `ansible_facts[register_as]` - Upgrade/readiness check task result
- `ansible_facts[register_as + '_task_id']` - Task ID for monitoring
- `ansible_facts[register_as + '_status']` - Final task status (when wait_for_completion is true)

## Example Output

```yaml
ansible_facts:
  device_upgrade:
    metadata:
      task:
        id: "task-uuid-1"
        name: "Device Upgrade"
  
  device_upgrade_task_id: "task-uuid-1"

  device_upgrade_status:
    status: "COMPLETED"
    message: "Upgrade completed successfully"
```

## Readiness Check vs. Upgrade

### Readiness Check (`readiness_check_only: true`)
- Validates devices are ready for upgrade
- Checks for issues like database integrity, version inconsistencies
- Faster execution (typically 5-15 minutes)
- Should always be run before actual upgrade

### Full Upgrade (`readiness_check_only: false`)
- Performs the actual upgrade process
- Much longer execution time (30-60+ minutes)
- Includes device reboot and configuration validation
- Should only be run after successful readiness check

## Error Handling

The role includes comprehensive error handling:

- Validates required variables before execution
- Monitors upgrade progress with configurable retries
- Provides meaningful error messages for failures
- Optionally verifies successful completion
- Supports upgrade revert options for recovery

## Best Practices

1. **Always run readiness check first**: Use `readiness_check_only: true` before actual upgrades
2. **Monitor progress**: Enable `wait_for_completion: true` for production environments
3. **Enable revert options**: Keep `enable_upgrade_revert: true` for safety
4. **Adjust timeouts**: Increase `max_retries` and `retry_delay` for slower environments
5. **Save logs**: Use `save_to_file: true` for audit trails

## License

GPL-3.0-or-later
