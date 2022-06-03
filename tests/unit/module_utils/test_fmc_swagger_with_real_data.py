from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json
import os
import unittest

from ansible_collections.cisco.fmcansible.plugins.module_utils.fmc_swagger_client import FmcSwaggerValidator, FmcSwaggerParser
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
TEST_DATA_FOLDER = os.path.join(DIR_PATH, 'test_data')


class TestFmcSwagger(unittest.TestCase):

    def setUp(self):
        self.init_mock_data()

    def init_mock_data(self):
        with open(os.path.join(TEST_DATA_FOLDER, 'fmc_spec_with_ex.json'), 'rb') as f:
            self.base_data = json.loads(f.read().decode('utf-8'))

    def test_with_all_data(self):
        fmc_data = FmcSwaggerParser().parse_spec(self.base_data)
        validator = FmcSwaggerValidator(fmc_data)
        models = fmc_data['models']
        operations = fmc_data['operations']

        invalid = set({})
        for operation in operations:
            model_name = operations[operation]['modelName']
            method = operations[operation]['method']
            if method != 'get' and model_name in models:
                if 'example' in models[model_name]:
                    example = models[model_name]['example']
                    try:
                        valid, rez = validator.validate_data(operation, example)
                        assert valid
                    except Exception:
                        invalid.add(model_name)
        assert invalid == set(['FTDManualNatRule'])

    def test_parse_all_data(self):
        fmc_data = FmcSwaggerParser().parse_spec(self.base_data)
        operations = fmc_data['operations']
        without_model_name = []
        expected_operations_counter = 0
        for key in self.base_data['paths']:
            operation = self.base_data['paths'][key]
            for __ in operation:
                expected_operations_counter += 1

        for key in operations:
            operation = operations[key]
            if not operation['modelName']:
                without_model_name.append(operation['url'])

        assert sorted(['/api/fmc_config/v1/domain/{domainUUID}/object/intrusionrules',
                       '/api/fmc_config/v1/domain/{domainUUID}/object/dynamicobjectmappings',
                       '/api/fmc_config/v1/domain/{domainUUID}/policy/prefilterpolicies/{containerUUID}/prefilterrules',
                       '/api/fmc_config/v1/domain/{domainUUID}/object/intrusionrulesupload',
                       '/api/fmc_config/v1/domain/{domainUUID}/policy/accesspolicies/{containerUUID}/accessrules',
                       '/api/fmc_config/v1/domain/{domainUUID}/object/dynamicobjects/{objectId}/mappings',
                       '/api/fmc_config/v1/domain/{domainUUID}/object/dynamicobjects']) == sorted(without_model_name)
        for key in fmc_data['model_operations'][None].keys():
            assert key == 'createSnort3IPSRulesFileUpload' or key.startswith("deleteMultiple")
        assert expected_operations_counter == len(operations)
