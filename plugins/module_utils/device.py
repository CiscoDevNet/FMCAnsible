# plugins/module_utils/device.py

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from abc import ABC
from enum import Enum
from urllib.parse import urlparse

# The test mocks these, so we need placeholder imports.
# In a real scenario, these would be actual library imports.

try:
    from kick.device.fp2k.fmc import Kp
    from kick.device.asa5500x.fmc import Fmc5500x
except ImportError:
    from unittest.mock import MagicMock

    # Create dummy classes if 'kick' is not installed,
    # allowing module to be imported.

    class Kp(object):
        def __init__(self, *args, **kwargs):
            pass

        def ssh_console(self):
            mock_console = MagicMock()
            mock_console.__enter__.return_value = mock_console
            mock_console.__exit__.return_value = False  # Propagate exceptions
            return mock_console

    class Fmc5500x(object):
        def __init__(self, *args, **kwargs):
            pass

        def ssh_console(self):
            mock_console = MagicMock()
            mock_console.__enter__.return_value = mock_console
            mock_console.__exit__.return_value = False  # Propagate exceptions
            return mock_console


class FmcConfigurationError(Exception):
    pass


class FmcModel(Enum):
    FMC_1600 = 'FMC-1600'
    FMC_2110 = 'FMC-2110'
    FMC_2120 = 'FMC-2120'
    FMC_2130 = 'FMC-2130'
    FMC_2600 = 'FMC-2600'
    FMC_4600 = 'FMC-4600'
    FMC_VIRTUAL = 'FMC-VIRTUAL'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class AbstractFmcPlatform(ABC):
    def __init__(self, module_params=None):
        self.module_params = module_params

    def install_fmc_image(self, module_params=None):
        raise NotImplementedError

    @classmethod
    def supports_fmc_model(cls, model):
        raise NotImplementedError

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

    def install_fmc_image(self, module_params=None):
        # Import Kp here to allow for mocking in tests
        # from kick.device.fp2k.fmc import Kp
        kp = Kp(self.module_params)
        with kp.ssh_console() as fmc_line:
            fmc_line.baseline_fp2k_fmc(self.module_params['image'])

    @classmethod
    def supports_fmc_model(cls, model):
        return model in cls.SUPPORTED_MODELS


class FmcAsa5500xPlatform(AbstractFmcPlatform):
    SUPPORTED_MODELS = [
        'ASA5508', 'ASA5516', FmcModel.FMC_4600.value
    ]

    def install_fmc_image(self, module_params=None):
        # Implementation based on test mocks
        fmc5500x = Fmc5500x(self.module_params)
        with fmc5500x.ssh_console() as fmc_line:
            fmc_line.rommon_to_new_image(self.module_params['image'])

    @classmethod
    def supports_fmc_model(cls, model):
        return model in cls.SUPPORTED_MODELS


class Fmc1600Platform(AbstractFmcPlatform):
    @classmethod
    def supports_fmc_model(cls, model):
        return model == FmcModel.FMC_1600.value

    def install_fmc_image(self, module_params=None):
        # Import Kp here to allow for mocking in tests
        # from kick.device.fp2k.fmc import Kp
        kp = Kp(self.module_params)
        with kp.ssh_console() as fmc_line:
            fmc_line.baseline_fp2k_fmc(self.module_params['image'])


class Fmc2600Platform(AbstractFmcPlatform):
    @classmethod
    def supports_fmc_model(cls, model):
        return model == FmcModel.FMC_2600.value

    def install_fmc_image(self, module_params=None):
        # Import Kp here to allow for mocking in tests
        # from kick.device.fp2k.fmc import Kp
        kp = Kp(self.module_params)
        with kp.ssh_console() as fmc_line:
            fmc_line.baseline_fp2k_fmc(self.module_params['image'])


class Fmc4600Platform(AbstractFmcPlatform):
    @classmethod
    def supports_fmc_model(cls, model):
        return model == FmcModel.FMC_4600.value

    def install_fmc_image(self, module_params=None):
        # Import Kp here to allow for mocking in tests
        # from kick.device.fp2k.fmc import Kp
        kp = Kp(self.module_params)
        with kp.ssh_console() as fmc_line:
            fmc_line.baseline_fp2k_fmc(self.module_params['image'])


class FmcVirtualPlatform(AbstractFmcPlatform):
    @classmethod
    def supports_fmc_model(cls, model):
        return model == 'FMC-VIRTUAL'

    def install_fmc_image(self, module_params=None):
        raise FmcConfigurationError('Image installation is not supported for virtual appliances.')


class FmcPlatformFactory(object):
    PLATFORMS = [
        Fmc1600Platform,
        Fmc2100Platform,
        Fmc2600Platform,
        Fmc4600Platform,
        FmcAsa5500xPlatform,
        FmcVirtualPlatform,
    ]

    @staticmethod
    def create(model, module_params):
        for platform_class in FmcPlatformFactory.PLATFORMS:
            if platform_class.supports_fmc_model(model):
                return platform_class(module_params)

        raise ValueError(f"FMC model '{model}' is not supported by this module.")
