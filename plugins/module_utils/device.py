# plugins/module_utils/device.py

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from abc import ABC, abstractmethod
from enum import Enum
from urllib.parse import urlparse

# The test mocks these, so we need placeholder imports.
# In a real scenario, these would be actual library imports.

try:
    from kick.device.fp2k.fmc import Kp
    from kick.device.asa5500x.fmc import Fmc5500x
except ImportError:
    # Create dummy classes if 'kick' is not installed,
    # allowing module to be imported.
    Kp = type('Kp', (object,), {})
    Fmc5500x = type('Fmc5500x', (object,), {})


class FmcModel(Enum):
    FMC_1600 = 'FMC-1600'
    FMC_2110 = 'FMC-2110'
    FMC_2120 = 'FMC-2120'
    FMC_2130 = 'FMC-2130'
    FMC_2600 = 'FMC-2600'
    FMC_4600 = 'FMC-4600'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class AbstractFmcPlatform(ABC):
    @abstractmethod
    def install_fmc_image(self, module_params):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def supports_fmc_model(cls, model):
        return False

    @staticmethod
    def parse_rommon_file_location(location):
        parsed_url = urlparse(location)
        if parsed_url.scheme != 'tftp':
            raise ValueError('The ROMMON image must be downloaded from TFTP server')
        return parsed_url.hostname, parsed_url.path


class Fmc2100Platform(AbstractFmcPlatform):
    SUPPORTED_MODELS = [
        FmcModel.FMC_2110.value,
        FmcModel.FMC_2120.value,
        FmcModel.FMC_2130.value,
    ]

    def install_fmc_image(self, module_params):
        # Implementation based on test mocks
        kp = Kp(module_params)
        with kp.ssh_console() as fmc_line:
            fmc_line.baseline_fp2k_fmc(module_params['image'])

    @classmethod
    def supports_fmc_model(cls, model):
        return model in cls.SUPPORTED_MODELS


class FmcAsa5500xPlatform(AbstractFmcPlatform):
    SUPPORTED_MODELS = [
        FmcModel.FMC_1600.value,
        FmcModel.FMC_2600.value,
        FmcModel.FMC_4600.value,
    ]

    def install_fmc_image(self, module_params):
        # Implementation based on test mocks
        fmc5500x = Fmc5500x(module_params)
        with fmc5500x.ssh_console() as fmc_line:
            fmc_line.rommon_to_new_image(module_params['image'])

    @classmethod
    def supports_fmc_model(cls, model):
        return model in cls.SUPPORTED_MODELS


class FmcPlatformFactory(object):
    PLATFORM_MAPPING = [
        (FmcAsa5500xPlatform, FmcAsa5500xPlatform.SUPPORTED_MODELS),
        (Fmc2100Platform, Fmc2100Platform.SUPPORTED_MODELS),
    ]

    @staticmethod
    def create(model, module_params):
        for platform_class, supported_models in FmcPlatformFactory.PLATFORM_MAPPING:
            if model in supported_models:
                return platform_class()

        raise ValueError(f"FMC model '{model}' is not supported by this module.")
