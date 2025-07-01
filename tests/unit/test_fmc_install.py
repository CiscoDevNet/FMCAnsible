# tests/unit/test_fmc_install.py

from __future__ import absolute_import, division, print_function

__metaclass__ = type

# Default parameters used across various unit tests.
# These represent typical inputs to the Ansible module.
DEFAULT_MODULE_PARAMS = {
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
    'image': 'tftp://10.0.0.1/images/fmc-image.pkg',
    'model': 'FMC-2600',
    'state': 'present',
}
