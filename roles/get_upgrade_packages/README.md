# Get Upgrade Packages Role

This Ansible role retrieves upgrade packages from Cisco Firepower Management Center (FMC) with optional filtering by version.

## Requirements

- Ansible 2.10 or higher
- cisco.fmcansible collection

## Role Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `register_as` | Name to register the upgrade packages as | `upgrade_packages` |
| `output_dir` | Directory where JSON output files will be saved | `.` (current directory) |
| `save_to_file` | Whether to save the package list to a file | `false` |
| `version_filter` | String to filter packages by version/name | `""` (empty) |
| `filter_by_version` | Whether to apply version filtering | `false` |

## Example Playbook

```yaml
- name: Get FMC Upgrade Packages
  hosts: fmc
  gather_facts: no
  connection: httpapi
  collections:
    - cisco.fmcansible
  
  roles:
    - role: get_upgrade_packages
      vars:
        version_filter: "7.7.0"
        filter_by_version: true
        save_to_file: true
```

## Return Values

The role sets the following facts:

- `ansible_facts[register_as]` - List of all upgrade packages
- `ansible_facts[register_as + '_filtered']` - Filtered package object (when filtering is enabled)

## Example Output

```yaml
ansible_facts:
  upgrade_packages:
    - id: "package-uuid-1"
      name: "Cisco_FTD_SSP_FP2K_Upgrade-7.7.0-89-Hotfix_A.sh"
      version: "7.7.0.89"
    - id: "package-uuid-2"
      name: "Cisco_FTD_SSP_FP2K_Upgrade-7.6.0-1-Hotfix_B.sh"
      version: "7.6.0.1"

  upgrade_packages_filtered:
    id: "package-uuid-1"
    name: "Cisco_FTD_SSP_FP2K_Upgrade-7.7.0-89-Hotfix_A.sh"
    version: "7.7.0.89"
```

## License

GPL-3.0-or-later
