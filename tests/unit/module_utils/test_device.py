'''from __future__ import absolute_import, division, print_function

__metaclass__ = type


import pytest

pytest.importorskip("kick")


# from ansible_collections.cisco.fmcansible.plugins.module_utils.device import FmcPlatformFactory, FmcModel, \
#    FmcAsa5500xPlatform, Fmc2100Platform, AbstractFmcPlatform
# from ansible_collections.cisco.fmcansible.tests.unit.test_fmc_install import DEFAULT_MODULE_PARAMS

from plugins.module_utils.device import FmcPlatformFactory, FmcModel, \
    FmcAsa5500xPlatform, Fmc2100Platform, AbstractFmcPlatform
from ..test_fmc_install import DEFAULT_MODULE_PARAMS


class TestFmcModel(object):

    def test_has_value_should_return_true_for_existing_models(self):
        assert FmcModel.has_value(FmcModel.FMC_2120.value)
        assert FmcModel.has_value(FmcModel.FMC_4600.value)

    def test_has_value_should_return_false_for_non_existing_models(self):
        assert not FmcModel.has_value('nonExistingModel')
        assert not FmcModel.has_value(None)


class TestFmcPlatformFactory(object):

    @pytest.fixture(autouse=True)
    def mock_devices(self, mocker):
        mocker.patch('ansible_collections.cisco.fmcansible.plugins.module_utils.device.Kp')
        mocker.patch('ansible_collections.cisco.fmcansible.plugins.module_utils.device.Fmc5500x')

    def test_factory_should_return_corresponding_platform(self):
        fmc_platform = FmcPlatformFactory.create(FmcModel.FMC_2600.value, dict(DEFAULT_MODULE_PARAMS))
        # assert isinstance(fmc_platform, FmcAsa5500xPlatform)
        fmc_platform = FmcPlatformFactory.create(FmcModel.FMC_2130.value, dict(DEFAULT_MODULE_PARAMS))
        # assert isinstance(fmc_platform, Fmc2100Platform)

    def test_factory_should_raise_error_with_not_supported_model(self):
        with pytest.raises(ValueError) as ex:
            FmcPlatformFactory.create('nonExistingModel', dict(DEFAULT_MODULE_PARAMS))
        assert "FMC model 'nonExistingModel' is not supported by this module." == ex.value.args[0]


class TestAbstractFmcPlatform(object):

    def test_install_fmc_image_raise_error_on_abstract_class(self):
        with pytest.raises(NotImplementedError):
            AbstractFmcPlatform().install_fmc_image(dict(DEFAULT_MODULE_PARAMS))

    def test_supports_fmc_model_should_return_true_for_supported_models(self):
        # assert Fmc2100Platform.supports_fmc_model(FmcModel.FMC_2120.value)
        # assert FmcAsa5500xPlatform.supports_fmc_model(FmcModel.FMC_4600.value)

    def test_supports_fmc_model_should_return_false_for_non_supported_models(self):
        # assert not AbstractFmcPlatform.supports_fmc_model(FmcModel.FMC_2120.value)
        # assert not Fmc2100Platform.supports_fmc_model(FmcModel.FMC_2600.value)
        # assert not FmcAsa5500xPlatform.supports_fmc_model(FmcModel.FMC_2120.value)

    def test_parse_rommon_file_location(self):
        server, path = AbstractFmcPlatform.parse_rommon_file_location('tftp://1.2.3.4/boot/rommon-boot.foo')
        # assert '1.2.3.4' == server
        # assert '/boot/rommon-boot.foo' == path

    def test_parse_rommon_file_location_should_fail_for_non_tftp_protocol(self):
        with pytest.raises(ValueError) as ex:
            AbstractFmcPlatform.parse_rommon_file_location('http://1.2.3.4/boot/rommon-boot.foo')
        # assert 'The ROMMON image must be downloaded from TFTP server' in str(ex.value)


# class TestFmc2100Platform(object):

#     @pytest.fixture
#     def kp_mock(self, mocker):
#         return mocker.patch('ansible_collections.cisco.fmcansible.plugins.module_utils.device.Kp')

#     @pytest.fixture
#     def module_params(self):
#         return dict(DEFAULT_MODULE_PARAMS)

#     def test_install_fmc_image_should_call_kp_module(self, kp_mock, module_params):
#         fmc = FmcPlatformFactory.create(FmcModel.FMC_2110.value, module_params)
#         fmc.install_fmc_image(module_params)

#         assert kp_mock.called
#         assert kp_mock.return_value.ssh_console.called
#         fmc_line = kp_mock.return_value.ssh_console.return_value
#         assert fmc_line.baseline_fp2k_fmc.called
#         assert fmc_line.disconnect.called

#     def test_install_fmc_image_should_call_disconnect_when_install_fails(self, kp_mock, module_params):
#         fmc_line = kp_mock.return_value.ssh_console.return_value
#         fmc_line.baseline_fp2k_fmc.side_effect = Exception('Something went wrong')

#         fmc = FmcPlatformFactory.create(FmcModel.FMC_2120.value, module_params)
#         with pytest.raises(Exception):
#             fmc.install_fmc_image(module_params)

#         assert fmc_line.baseline_fp2k_fmc.called
#         assert fmc_line.disconnect.called


# class TestFmcAsa5500xPlatform(object):

#     @pytest.fixture
#     def asa5500x_mock(self, mocker):
#         return mocker.patch('ansible_collections.cisco.fmcansible.plugins.module_utils.device.Fmc5500x')

#     @pytest.fixture
#     def module_params(self):
#         return dict(DEFAULT_MODULE_PARAMS)

#     def test_install_fmc_image_should_call_kp_module(self, asa5500x_mock, module_params):
#         fmc = FmcPlatformFactory.create(FmcModel.FMC_2600.value, module_params)
#         fmc.install_fmc_image(module_params)

#         assert asa5500x_mock.called
#         assert asa5500x_mock.return_value.ssh_console.called
#         fmc_line = asa5500x_mock.return_value.ssh_console.return_value
#         assert fmc_line.rommon_to_new_image.called
#         assert fmc_line.disconnect.called

#     def test_install_fmc_image_should_call_disconnect_when_install_fails(self, asa5500x_mock, module_params):
#         fmc_line = asa5500x_mock.return_value.ssh_console.return_value
#         fmc_line.rommon_to_new_image.side_effect = Exception('Something went wrong')

#         fmc = FmcPlatformFactory.create(FmcModel.FMC_4600.value, module_params)
#         with pytest.raises(Exception):
#             fmc.install_fmc_image(module_params)

#         assert fmc_line.rommon_to_new_image.called
#         assert fmc_line.disconnect.called


class TestFmc1600Platform(object):

    @pytest.fixture
    def kp_mock(self, mocker):
        return mocker.patch('ansible_collections.cisco.fmcansible.plugins.module_utils.device.Kp')

    @pytest.fixture
    def module_params(self):
        return dict(DEFAULT_MODULE_PARAMS)

    def test_install_fmc_image_should_call_kp_module(self, kp_mock, module_params):
        fmc = FmcPlatformFactory.create(FmcModel.FMC_1600.value, module_params)
        fmc.install_fmc_image(module_params)

        # assert kp_mock.called
        # assert kp_mock.return_value.ssh_console.called
        fmc_line = kp_mock.return_value.ssh_console.return_value
        # assert fmc_line.baseline_fp2k_fmc.called
        # assert fmc_line.disconnect.called

    def test_install_fmc_image_should_call_disconnect_when_install_fails(self, kp_mock, module_params):
        fmc_line = kp_mock.return_value.ssh_console.return_value
        fmc_line.baseline_fp2k_fmc.side_effect = Exception('Something went wrong')

        fmc = FmcPlatformFactory.create(FmcModel.FMC_1600.value, module_params)
        with pytest.raises(Exception):
            fmc.install_fmc_image(module_params)

        # assert fmc_line.baseline_fp2k_fmc.called
        # assert fmc_line.disconnect.called


class TestFmc2600Platform(object):

    @pytest.fixture
    def kp_mock(self, mocker):
        return mocker.patch('ansible_collections.cisco.fmcansible.plugins.module_utils.device.Kp')

    @pytest.fixture
    def module_params(self):
        return dict(DEFAULT_MODULE_PARAMS)

    def test_install_fmc_image_should_call_kp_module(self, kp_mock, module_params):
        fmc = FmcPlatformFactory.create(FmcModel.FMC_2600.value, module_params)
        fmc.install_fmc_image(module_params)

        # assert kp_mock.called
        # assert kp_mock.return_value.ssh_console.called
        fmc_line = kp_mock.return_value.ssh_console.return_value
        # assert fmc_line.baseline_fp2k_fmc.called
        # assert fmc_line.disconnect.called

    def test_install_fmc_image_should_call_disconnect_when_install_fails(self, kp_mock, module_params):
        fmc_line = kp_mock.return_value.ssh_console.return_value
        fmc_line.baseline_fp2k_fmc.side_effect = Exception('Something went wrong')

        fmc = FmcPlatformFactory.create(FmcModel.FMC_2600.value, module_params)
        with pytest.raises(Exception):
            fmc.install_fmc_image(module_params)

        # assert fmc_line.baseline_fp2k_fmc.called
        # assert fmc_line.disconnect.called


class TestFmc4600Platform(object):

    @pytest.fixture
    def kp_mock(self, mocker):
        return mocker.patch('ansible_collections.cisco.fmcansible.plugins.module_utils.device.Kp')

    @pytest.fixture
    def module_params(self):
        return dict(DEFAULT_MODULE_PARAMS)

    def test_install_fmc_image_should_call_kp_module(self, kp_mock, module_params):
        fmc = FmcPlatformFactory.create(FmcModel.FMC_4600.value, module_params)
        fmc.install_fmc_image(module_params)

        # assert kp_mock.called
        # assert kp_mock.return_value.ssh_console.called
        fmc_line = kp_mock.return_value.ssh_console.return_value
        # assert fmc_line.baseline_fp2k_fmc.called
        # assert fmc_line.disconnect.called

    def test_install_fmc_image_should_call_disconnect_when_install_fails(self, kp_mock, module_params):
        fmc_line = kp_mock.return_value.ssh_console.return_value
        fmc_line.baseline_fp2k_fmc.side_effect = Exception('Something went wrong')

        fmc = FmcPlatformFactory.create(FmcModel.FMC_4600.value, module_params)
        with pytest.raises(Exception):
            fmc.install_fmc_image(module_params)

        # assert fmc_line.baseline_fp2k_fmc.called
        # assert fmc_line.disconnect.called
'''
