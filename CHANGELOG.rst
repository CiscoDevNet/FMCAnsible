=========================================
Cisco FMCAnsible Collection Release Notes
=========================================

.. contents:: Topics

v1.1.1
======

Release Summary
---------------

Maintenance release fixing long-running on-prem FMC authentication, upsert
query-parameter handling, and Swagger request validation.

Breaking Changes / Porting Guide
--------------------------------

- The minimum supported version is now ``ansible-core 2.16``. Environments
  using older Ansible releases must upgrade Ansible before installing this
  collection version.

Minor Changes
-------------

- Removed unused ``community.general`` and ``community.network`` collection
  dependencies. ``ansible.netcommon`` now requires version 8.5.2 or later, and
  ``ansible.utils`` requires version 5.1.2 or later.
- Replaced deprecated ``ansible.module_utils.six`` compatibility imports with
  native Python 3 equivalents for current Ansible sanity compatibility.
- Updated Python and Ansible content to pass the Galaxy importer flake8 and
  ansible-lint checks.
- Corrected bulk network and URL object examples, documented the dedicated
  on-prem FMC API-user requirement, clarified loop result registration, and
  linked the generated API operation index. Documented the current true-bulk
  idempotency limitation and the single-object upsert workaround.

Bugfixes
--------

- Automatically refresh expired on-prem FMC access tokens and retry the
  interrupted API request. If the refresh token is invalid or exhausted,
  authenticate again using the configured FMC credentials.
- Keep cdFMC/SCC bearer-token authentication separate from the on-prem FMC
  username/password refresh and reauthentication workflow.
- Preserve operation-specific query parameters when an upsert performs its
  GETALL lookup, including parameters such as access-policy category
  ``section``.
- Correct Swagger validation for free-form objects while continuing to validate
  explicitly defined fields and fields required by request examples.


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
