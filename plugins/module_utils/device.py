# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from enum import Enum
from ansible.module_utils.six.moves.urllib.parse import urlparse

try:
    from kick.device2.fmc5500x.actions.fmc5500x import Fmc5500x
    from kick.device2.kp.actions import Kp

    HAS_KICK = True
except ImportError:
    HAS_KICK = False


class FmcModel(Enum):
    FMC_1600 = 'Cisco Firewall Management Center 1600'
    FMC_2600 = 'Cisco Firewall Management Center 2600'
    FMC_4600 = 'Cisco Firewall Management Center 4600'

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)


class FmcPlatformFactory(object):

    @staticmethod
    def create(model, module_params):
        for cls in AbstractFmcPlatform.__subclasses__():
            if cls.supports_fmc_model(model):
                return cls(module_params)
        raise ValueError("FMC model '%s' is not supported by this module." % model)


class AbstractFmcPlatform(object):
    PLATFORM_MODELS = []

    def install_fmc_image(self, params):
        raise NotImplementedError('The method should be overridden in subclass')

    @classmethod
    def supports_fmc_model(cls, model):
        return any(model == item.value for item in cls.PLATFORM_MODELS)

    @staticmethod
    def parse_rommon_file_location(rommon_file_location):
        rommon_url = urlparse(rommon_file_location)
        if rommon_url.scheme != 'tftp':
            raise ValueError('The ROMMON image must be downloaded from TFTP server, other protocols are not supported.')
        return rommon_url.netloc, rommon_url.path


class Fmc2100Platform(AbstractFmcPlatform):
    PLATFORM_MODELS = [FmcModel.FMC_1600, FmcModel.FMC_2600, FmcModel.FMC_4600]

    def __init__(self, params):
        self._fmc = Kp(hostname=params["device_hostname"],
                       login_username=params["device_username"],
                       login_password=params["device_password"],
                       sudo_password=params.get("device_sudo_password") or params["device_password"])

    def install_fmc_image(self, params):
        line = self._fmc.ssh_console(ip=params["console_ip"],
                                     port=params["console_port"],
                                     username=params["console_username"],
                                     password=params["console_password"])

        try:
            rommon_server, rommon_path = self.parse_rommon_file_location(params["rommon_file_location"])
            line.baseline_fp2k_fmc(tftp_server=rommon_server,
                                   rommon_file=rommon_path,
                                   uut_hostname=params["device_hostname"],
                                   uut_username=params["device_username"],
                                   uut_password=params.get("device_new_password") or params["device_password"],
                                   uut_ip=params["device_ip"],
                                   uut_netmask=params["device_netmask"],
                                   uut_gateway=params["device_gateway"],
                                   dns_servers=params["dns_server"],
                                   search_domains=params["search_domains"],
                                   fxos_url=params["image_file_location"],
                                   fmc_version=params["image_version"])
        finally:
            line.disconnect()


class FmcAsa5500xPlatform(AbstractFmcPlatform):
    PLATFORM_MODELS = [FmcModel.FMC_1600, FmcModel.FMC_2600, FmcModel.FMC_4600]

    def __init__(self, params):
        self._fmc = Fmc5500x(hostname=params["device_hostname"],
                             login_password=params["device_password"],
                             sudo_password=params.get("device_sudo_password") or params["device_password"])

    def install_fmc_image(self, params):
        line = self._fmc.ssh_console(ip=params["console_ip"],
                                     port=params["console_port"],
                                     username=params["console_username"],
                                     password=params["console_password"])
        try:
            rommon_server, rommon_path = self.parse_rommon_file_location(params["rommon_file_location"])
            line.rommon_to_new_image(rommon_tftp_server=rommon_server,
                                     rommon_image=rommon_path,
                                     pkg_image=params["image_file_location"],
                                     uut_ip=params["device_ip"],
                                     uut_netmask=params["device_netmask"],
                                     uut_gateway=params["device_gateway"],
                                     dns_server=params["dns_server"],
                                     search_domains=params["search_domains"],
                                     hostname=params["device_hostname"])
        finally:
            line.disconnect()
