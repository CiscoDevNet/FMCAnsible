# Device Backup Role

This Ansible role creates and monitors device backups in Cisco Firepower Management Center (FMC).

## Requirements

- Ansible 2.10 or higher
- cisco.fmcansible collection

## Role Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `domain_uuid` | UUID of the FMC domain to use | Required - no default |
| `target_devices` | List of target devices/containers for backup | Required - no default |
| `register_as` | Name to register the backup result as | `device_backup` |
| `retrieve_to_fmc` | Whether to retrieve backup to FMC management center | `true` |
| `wait_for_completion` | Whether to wait for backup completion | `true` |
| `max_retries` | Maximum number of retries for status checks | `60` |
| `retry_delay` | Delay between status checks (seconds) | `30` |
| `verify_success` | Whether to verify backup completed successfully | `true` |
| `output_dir` | Directory where JSON output files will be saved | `.` (current directory) |
| `save_to_file` | Whether to save the backup task info to a file | `false` |

## Example Playbook

```yaml
- name: Backup FMC Devices
  hosts: fmc
  gather_facts: no
  connection: httpapi
  collections:
    - cisco.fmcansible
  
  roles:
    - role: device_backup
      vars:
        domain_uuid: "{{ domain_id }}"
        target_devices:
          - id: "device-uuid-1"
            type: "Device"
            name: "FTD-1"
          - id: "ha-container-uuid-1"
            type: "HAContainer"
            name: "HA-Pair-1"
        wait_for_completion: true
        verify_success: true
        save_to_file: true
```

## Return Values

The role sets the following facts:

- `ansible_facts[register_as]` - Backup task result
- `ansible_facts[register_as + '_task_id']` - Task ID for monitoring
- `ansible_facts[register_as + '_status']` - Final backup status (when wait_for_completion is true)

## Example Output

```yaml
ansible_facts:
  device_backup:
    metadata:
      task:
        id: "task-uuid-1"
        name: "Device Backup"
  
  device_backup_task_id: "task-uuid-1"

  device_backup_status:
    status: "COMPLETED"
    message: "Backup completed successfully"
```

## Error Handling

The role includes comprehensive error handling:

- Validates required variables before execution
- Monitors backup progress with configurable retries
- Provides meaningful error messages for failures
- Optionally verifies successful completion

## License

GPL-3.0-or-later
