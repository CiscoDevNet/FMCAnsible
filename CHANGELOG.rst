=========================================
Cisco FMCAnsible Collection Release Notes
=========================================

.. contents:: Topics

v1.1.0
======

Release Summary
---------------

First stable release of the 1.x line, promoting the v1.0.10 pre-release changes
and adding full documentation for facts gathering.

Minor Changes
-------------

- Promoted ``fmc_facts`` module to stable; supports facts gathering for domains, devices, access policies, intrusion policies, and file policies.
- Added documentation and usage guide for the ``fmc_facts`` module.
- Improved sample playbooks and inventory examples for both traditional FMC and cdFMC workflows.
- Validated compatibility with Cisco Secure FMC versions 7.2, 7.3, 7.4, 7.6, and 10.0.

Bugfixes
--------

- Fixed ``common.py`` equal-objects comparison to correctly handle nested object structures (multiple iterative fixes).
- Applied PEP 8 and Ansible sanity-check fixes across module utils and plugins.
- Corrected ``ansible.cfg`` base configuration to avoid installing into a root folder.
- Improved ``device_upgrade`` role task polling and removed unused variables.


v1.0.10
=======

Release Summary
---------------

Pre-release adding the ``fmc_facts`` facts-gathering module and iterative fixes to
``common.py`` and sanity checks.

Minor Changes
-------------

- Added new ``fmc_facts`` module for structured facts gathering.
- Extended facts gathering to cover intrusion policies and file policies.
- Modified sample playbooks to demonstrate the new facts module.
- Added unit tests for the facts gathering module.
- Added documentation for cdFMC (``ansible.cfg``) and updated base configuration.
- Added ``fmc_facts`` usage documentation.

Bugfixes
--------

- Multiple iterative fixes to ``common.py`` equal-objects comparison logic.
- PEP 8 and sanity-check fixes across the collection (plugins and module utils).
- Fixed ``device_upgrade`` role task polling; removed unused variables.


v1.0.8
======

Release Summary
---------------

Major feature release adding Cisco Defense FMC (cdFMC) support with Bearer token
authentication, FTD HA Upgrade automation, and access policy enhancements.

Major Changes
-------------

- Added Cisco Defense FMC (cdFMC) support with Bearer token authentication.
- Added roles for FTD HA Upgrade user experience automation.

Minor Changes
-------------

- Added FTD HA Upgrade sample playbook.
- Added ``fmc_access_policies`` module and feature access policy support.
- Removed caching test cache.

Bugfixes
--------

- Fixed CI pipeline issues.


v1.0.6
======

Release Summary
---------------

Pre-release with PEP 8 compliance fixes to ``fmc_configuration.py``.

Bugfixes
--------

- Applied PEP 8 updates to ``fmc_configuration.py``.


v1.0.4
======

Release Summary
---------------

Documentation update release.

Minor Changes
-------------

- Updated README with latest usage instructions.


v1.0.2
======

Release Summary
---------------

Merged development branch into main.


v1.0.0
======

Release Summary
---------------

Initial 1.0 stable release introducing Cisco Defense FMC (cdFMC) support.

Major Changes
-------------

- Added cdFMC support as the foundation for the 1.x release line.


v0.1.0
======

Release Summary
---------------

This is the first release of the ``cisco.fmcansible`` collection.

