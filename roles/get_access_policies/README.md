# Get Access Policies Role

This Ansible role collects and processes access policies from Cisco Firepower Management Center (FMC). It provides a structured approach to retrieving access policies, their rules, and the objects referenced within those rules.

## Requirements

- Ansible 2.10 or higher
- cisco.fmcansible collection

## Role Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `domain_uuid` | UUID of the FMC domain to use | Required - no default |
| `output_dir` | Directory where JSON output files will be saved | `.` (current directory) |
| `object_depth` | How deep to retrieve nested objects (1 = direct objects only, 2+ = retrieve nested objects) | `2` |
| `collect_ports` | Whether to collect port objects in addition to networks | `true` |
| `expanded` | Whether to retrieve expanded rule information | `true` |

## Example Playbook

```yaml
- name: Collect FMC Access Policies and Rules
  hosts: fmc
  gather_facts: no
  connection: httpapi
  collections:
    - cisco.fmcansible
  vars:
    domain_uuid: "your-domain-uuid-here"
    output_dir: "/tmp/fmc_policies"
    
  pre_tasks:
    - name: Ensure output directory exists
      file:
        path: "{{ output_dir }}"
        state: directory
      delegate_to: localhost
      run_once: true
      
  roles:
    - role: get_access_policies
      vars:
        object_depth: 2
        collect_ports: true
```

## Output

For each access policy processed, this role creates a JSON file named after the policy (with special characters replaced). Each file contains:

- Policy metadata (name, ID)
- All rules in the policy
- Network and port objects referenced in each rule (if configured)

Example output structure:
```json
{
  "name": "Example Policy",
  "id": "0050568C-21A8-0ed3-0000-068719476736",
  "rules": [
    {
      "name": "Allow Internal Traffic",
      "id": "0050568C-21A8-0ed3-0000-068719477299",
      "sourceNetworks": { ... },
      "destinationNetworks": { ... },
      "sourcePorts": { ... },
      "destinationPorts": { ... },
      "action": "ALLOW",
      "enabled": true
    }
  ]
}
```

## License

GPL-3.0-or-later
