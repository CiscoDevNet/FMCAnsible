# FMC Facts Module - Complete Guide

## Overview

The `fmc_facts` module enables `gather_facts: true` to work properly with FMC httpapi connections. It's designed with performance in mind, especially for large FMC deployments with many network objects, security zones, and other configuration elements.

## Quick Start

### Basic Usage (Recommended)
```yaml
- name: FMC Operations with automatic facts
  hosts: fmc_hosts
  connection: httpapi
  gather_facts: true  # Gets minimal facts automatically
  
  tasks:
    - name: Use auto-gathered facts
      cisco.fmcansible.fmc_configuration:
        operation: createNetworkObject
        data:
          name: "MyNetwork" 
          value: "192.168.1.0/24"
          type: "Network"
        path_params:
          domainUUID: "{{ ansible_facts.fmc.domains[0].uuid }}"
```

### Advanced Usage (Custom Subsets)
```yaml
- name: FMC Operations with custom facts
  hosts: fmc_hosts
  connection: httpapi
  gather_facts: false
  
  tasks:
    - name: Gather comprehensive facts
      cisco.fmcansible.fmc_facts:
        gather_subset: ['all']  # or specific subsets
        
    - name: Use comprehensive facts
      debug:
        msg: "Found {{ ansible_facts.fmc.network_objects[ansible_facts.fmc.domains[0].uuid] | length }} network objects"
```

## How It Works

### Automatic Facts Gathering 
When you set `gather_facts: true` in your playbook, Ansible automatically calls the FMC facts module with the `min` subset for optimal performance:

```yaml
- name: FMC Operations  
  hosts: fmc_hosts
  connection: httpapi
  gather_facts: true  # Always uses 'min' subset (domains, devices, access_policies)
  
  tasks:
    - name: Use auto-gathered facts
      debug:
        var: ansible_facts.fmc.domains
```

### Manual Facts Gathering
For fine-grained control over what facts are gathered, call the facts module explicitly:

```yaml
- name: Manual facts gathering
  cisco.fmcansible.fmc_facts:
    gather_subset: ['domains', 'network_objects']  # Custom subsets
```

## Controlling Facts Gathering

**Note**: Automatic facts gathering with `gather_facts: true` always uses the default `min` subset for performance. To use other subsets, use manual facts gathering.

```yaml
# Automatic facts gathering (always uses 'min' subset)
- name: Automatic facts (minimal only)
  hosts: fmc_hosts
  connection: httpapi  
  gather_facts: true  # Always gathers 'min' subset (domains, devices, access_policies)
  
  tasks:
    - name: Use auto-gathered minimal facts
      debug:
        var: ansible_facts.fmc.domains

# Manual facts gathering (full control)
- name: Custom facts gathering
  hosts: fmc_hosts
  connection: httpapi  
  gather_facts: false
  
  tasks:
    - name: Gather specific facts
      cisco.fmcansible.fmc_facts:
        gather_subset: ['all']  # or ['domains', 'devices', 'network_objects']
```

## Available Fact Subsets

| Subset                | Description                       | Performance | Use Case                          |
| --------------------- | --------------------------------- | ----------- | --------------------------------- |
| `min`                 | domains, devices, access_policies | ⚡ Fast      | Default, most common operations   |
| `domains`             | Domain information only           | ⚡ Very Fast | Basic domain info                 |
| `devices`             | Device information                | ⚡ Fast      | Device management                 |
| `access_policies`     | Access policy information         | ⚡ Fast      | Policy operations                 |
| `physical_interfaces` | Physical interface details        | 🟡 Medium    | Interface configuration           |
| `network_objects`     | Network objects                   | 🔴 Slow      | When working with network objects |
| `port_objects`        | Port objects                      | 🔴 Slow      | When working with port objects    |
| `security_zones`      | Security zones                    | 🟡 Medium    | Security zone operations          |
| `device_groups`       | Device groups                     | 🟡 Medium    | Device group management           |
| `all`                 | Everything above                  | 🔴 Very Slow | Complete environment analysis     |

## Performance Considerations

### API Call Impact

The module makes REST API calls to gather facts. The number of calls depends on your `gather_subset` configuration:

| gather_subset                           | API Calls         | Use Case                               |
| --------------------------------------- | ----------------- | -------------------------------------- |
| `min`                                   | 1 + (domains × 3) | **RECOMMENDED** - Essential facts only |
| `domains`, `devices`, `access_policies` | 1 + (domains × 3) | Good performance, basic facts          |
| `all`                                   | 1 + (domains × 7) | **USE WITH CAUTION** - Can be slow     |

### Dataset Size Impact

Some fact types can return large datasets that impact performance:

#### Fast Facts (Small datasets):
- `domains` - Usually < 10 domains
- `devices` - Typically < 100 devices per domain  
- `access_policies` - Usually < 50 policies per domain

#### Slow Facts (Large datasets):
- `network_objects` - Can be 1000+ objects per domain
- `security_zones` - Can be 100+ zones per domain
- `port_objects` - Can be 500+ objects per domain

## Recommendations

### 1. Use `min` by Default
```yaml
- name: Gather essential facts (RECOMMENDED)
  cisco.fmcansible.fmc_facts:
    gather_subset:
      - min  # domains, devices, access_policies only
```

### 2. Request Large Datasets Only When Needed
```yaml
# BAD - Gathers everything regardless of need
- cisco.fmcansible.fmc_facts:
    gather_subset: [all]

# GOOD - Only gather what you need
- cisco.fmcansible.fmc_facts:
    gather_subset: [domains, network_objects]  # Only when you need network objects
```

### 3. Use Physical Interfaces Conditionally
```yaml
- name: Gather interfaces only if devices exist
  cisco.fmcansible.fmc_facts:
    gather_subset:
      - domains
      - devices
      - physical_interfaces  # Only gathered if devices are present
```

### 4. Domain-Specific Gathering
```yaml
- name: Gather facts for specific domain
  cisco.fmcansible.fmc_facts:
    domain_uuid: "{{ target_domain_id }}"
    gather_subset: [network_objects]  # Faster than all domains
```

## Migration from Manual Fact Gathering

### Before (Multiple manual calls):
```yaml
- name: Get domains
  cisco.fmcansible.fmc_configuration:
    operation: getAllDomain
    register_as: domains

- name: Get devices  
  cisco.fmcansible.fmc_configuration:
    operation: getAllDevice
    path_params:
      domainUUID: "{{ domains[0].uuid }}"
    register_as: devices

# ... many more manual calls
```

### After (Single facts call):
```yaml
- name: Gather facts efficiently
  cisco.fmcansible.fmc_facts:
    gather_subset: [min]

# Use facts directly
- name: Configure device
  cisco.fmcansible.fmc_configuration:
    operation: updateDevice
    path_params:
      domainUUID: "{{ ansible_facts.fmc.domains[0].uuid }}"
      objectId: "{{ ansible_facts.fmc.devices[ansible_facts.fmc.domains[0].uuid][0].id }}"
```

## Facts Structure

Gathered facts are available in the `ansible_facts.fmc.*` namespace:

```yaml
ansible_facts:
  fmc:
    domains: 
      - name: "Global"
        uuid: "e276abec-e0f2-11e3-8169-6d9ed49b625f"
    devices:
      "e276abec-e0f2-11e3-8169-6d9ed49b625f":  # keyed by domain UUID
        - name: "FTD-01"
          id: "device-uuid-here"
          type: "Device"
    access_policies:
      "e276abec-e0f2-11e3-8169-6d9ed49b625f":  # keyed by domain UUID
        - name: "Access_Policy_1"
          id: "policy-uuid-here"
    # Additional facts when using larger subsets:
    network_objects:      # Available with 'network_objects' or 'all'
    physical_interfaces:  # Available with 'physical_interfaces' or 'all'
    port_objects:        # Available with 'port_objects' or 'all'
    security_zones:      # Available with 'security_zones' or 'all'
```

## Best Practices

1. **Start with `min`** - Use minimal facts unless you specifically need more
2. **Profile your workload** - Test performance with your FMC size
3. **Cache facts** - Reuse gathered facts across multiple tasks in the same play
4. **Avoid `all` in production** - Especially on large FMCs with many objects
5. **Request incrementally** - Add fact types only as needed
6. **Use domain filtering** - When working with specific domains only

## Troubleshooting

### Performance Issues

If fact gathering is slow:

1. **Check FMC size**: How many objects do you have?
2. **Use minimal subsets**: `gather_subset: [domains, devices]` instead of `[all]`
3. **Gather large datasets separately**:
   ```yaml
   # First - essential facts
   - cisco.fmcansible.fmc_facts:
       gather_subset: [min]
   
   # Later - large datasets if needed
   - cisco.fmcansible.fmc_facts:
       gather_subset: [domains, network_objects]
   ```
4. **Use domain-specific gathering**:
   ```yaml
   - cisco.fmcansible.fmc_facts:
       domain_uuid: "{{ specific_domain_id }}"
       gather_subset: [network_objects]
   ```

### Common Errors

**"No fact modules available for your network OS"**
- Add `facts_modules = cisco.fmcansible.fmc_facts` to your `ansible.cfg`

**Facts gathering is slow**
- Use `gather_subset: [min]` instead of `[all]`
- Check your FMC deployment size

**Missing network objects in automatic facts**
- Use manual facts gathering: `cisco.fmcansible.fmc_facts` with `gather_subset: [network_objects]`
- Automatic `gather_facts: true` only includes minimal facts for performance

## Examples

### Example 1: Basic Network Object Creation
```yaml
- name: Create network object with automatic facts
  hosts: fmc_hosts
  connection: httpapi
  gather_facts: true

  tasks:
    - name: Create network object
      cisco.fmcansible.fmc_configuration:
        operation: createNetworkObject
        data:
          name: "ServerNetwork"
          value: "10.1.1.0/24"
          type: "Network"
        path_params:
          domainUUID: "{{ ansible_facts.fmc.domains[0].uuid }}"
```

### Example 2: Working with Network Objects
```yaml
- name: Inventory existing network objects
  hosts: fmc_hosts
  connection: httpapi
  gather_facts: false

  tasks:
    - name: Gather network objects
      cisco.fmcansible.fmc_facts:
        gather_subset: ['domains', 'network_objects']
        
    - name: Display network objects
      debug:
        msg: "Domain {{ item.key }}: {{ item.value | length }} network objects"
      loop: "{{ ansible_facts.fmc.network_objects | dict2items }}"
```

### Example 3: Performance-Optimized Large Environment
```yaml
- name: Large FMC operations
  hosts: large_fmc
  connection: httpapi
  gather_facts: true  # Gets minimal facts quickly

  tasks:
    - name: Essential operations with minimal facts
      debug:
        msg: "Working with {{ ansible_facts.fmc.domains | length }} domains"

    - name: Gather network objects only when needed
      cisco.fmcansible.fmc_facts:
        gather_subset: [network_objects]
        domain_uuid: "{{ ansible_facts.fmc.domains[0].uuid }}"
      when: configure_network_objects | default(false)
```
