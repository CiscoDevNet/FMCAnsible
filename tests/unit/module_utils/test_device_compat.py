from __future__ import absolute_import, division, print_function

__metaclass__ = type

from enum import Enum

import pytest

from ansible_collections.cisco.fmcansible.plugins.module_utils.device import (
    AbstractFmcPlatform,
    FmcModel,
    FmcPlatformFactory,
    FmcVirtualPlatform,
    Kp,
)


def test_fmc_model_preserves_enum_behavior():
    assert isinstance(FmcModel.FMC_VIRTUAL, Enum)
    assert FmcModel.FMC_VIRTUAL.value == 'FMC-VIRTUAL'
    assert FmcModel('FMC-VIRTUAL') is FmcModel.FMC_VIRTUAL
    assert FmcModel.has_value('FMC-VIRTUAL')
    assert not FmcModel.has_value('not-a-model')


def test_factory_preserves_virtual_platform_selection():
    platform = FmcPlatformFactory.create('FMC-VIRTUAL', {})

    assert isinstance(platform, FmcVirtualPlatform)


def test_parse_rommon_file_location_preserves_validation():
    assert AbstractFmcPlatform.parse_rommon_file_location(
        'tftp://192.0.2.10/images/boot.img'
    ) == ('192.0.2.10', '/images/boot.img')

    with pytest.raises(ValueError):
        AbstractFmcPlatform.parse_rommon_file_location(
            'https://192.0.2.10/images/boot.img'
        )


def test_missing_kick_fallback_preserves_console_context_manager():
    console = Kp({}).ssh_console()

    assert console.__enter__.return_value is console
    assert console.__exit__.return_value is False
