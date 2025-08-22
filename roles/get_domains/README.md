# Get Domains Role

This Ansible role retrieves all FMC domains from Cisco Firepower Management Center (FMC).

## Requirements

- Ansible 2.10 or higher
- cisco.fmcansible collection

## Role Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `register_as` | Name to register the domains as in Ansible facts | `fmc_domains` |
| `output_dir` | Directory where JSON output files will be saved | `.` (current directory) |
| `save_to_file` | Whether to save the domain list to a file | `false` |

## Example Playbook

```yaml
- name: Get FMC Domains
  hosts: fmc
  gather_facts: no
  connection: httpapi
  collections:
    - cisco.fmcansible
    
  roles:
    - role: get_domains
      vars:
        save_to_file: true
        output_dir: "/tmp/fmc_data"
```

## Output

This role retrieves all FMC domains and registers them as an Ansible fact. The domains can be accessed via the variable name specified in `register_as` (default: `fmc_domains`).

Example accessing the first domain's UUID:
```yaml
- debug:
    msg: "First domain UUID: {{ fmc_domains[0].uuid }}"
```

## Files Generated

When `save_to_file` is set to `true`, this role creates:
- `fmc_domains.json` - Contains the complete domains response
