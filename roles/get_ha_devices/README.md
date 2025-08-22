# Get HA Devices Role

This Ansible role retrieves FTD HA device containers from Cisco Firepower Management Center (FMC) with optional filtering and target list building.

## Requirements

- Ansible 2.10 or higher
- cisco.fmcansible collection

## Role Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `domain_uuid` | UUID of the FMC domain to use | Required - no default |
| `register_as` | Name to register the HA devices as | `ha_devices` |
| `expanded` | Whether to retrieve expanded HA device information | `true` |
| `output_dir` | Directory where JSON output files will be saved | `.` (current directory) |
| `save_to_file` | Whether to save the HA devices list to a file | `false` |
| `ha_pair_names` | List of HA pair names to filter by | `[]` (empty list) |
| `filter_by_names` | Whether to apply name filtering | `false` |
| `build_target_lists` | Whether to build target container and device lists | `false` |

## Example Playbook

```yaml
- name: Get FMC HA Devices
  hosts: fmc
  gather_facts: no
  connection: httpapi
  collections:
    - cisco.fmcansible
  
  roles:
    - role: get_ha_devices
      vars:
        domain_uuid: "{{ domain_id }}"
        ha_pair_names:
          - "HA-Pair-1"
          - "HA-Pair-2"
        filter_by_names: true
        build_target_lists: true
        save_to_file: true
```

## Return Values

The role sets the following facts:

- `ansible_facts[register_as]` - List of all HA devices
- `ansible_facts[register_as + '_filtered']` - Filtered HA devices (when filtering is enabled)
- `ansible_facts[register_as + '_target_containers']` - Target container list for operations (when build_target_lists is true)
- `ansible_facts[register_as + '_target_devices']` - Target device list for operations (when build_target_lists is true)

## Example Output

```yaml
ansible_facts:
  ha_devices:
    - id: "ha-container-uuid-1"
      name: "HA-Pair-1"
      primary:
        id: "device-uuid-1"
        name: "FTD-Primary-1"
      secondary:
        id: "device-uuid-2"
        name: "FTD-Secondary-1"

  ha_devices_target_containers:
    - id: "ha-container-uuid-1"
      type: "HAContainer"
      name: "HA-Pair-1"

  ha_devices_target_devices:
    - id: "device-uuid-1"
      type: "Device"
      name: "FTD-Primary-1"
```

## License

GPL-3.0-or-later
