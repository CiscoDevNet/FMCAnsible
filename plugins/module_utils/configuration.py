# -*- coding: utf-8 -*-

# Copyright (c) 2018 Cisco and/or its affiliates.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import copy
from functools import partial

from ansible.module_utils.six import iteritems

from ansible_collections.cisco.fmcansible.plugins.module_utils.common import HTTPMethod, equal_objects, delete_props_not_in_model, \
    FmcServerError, ResponseParams, copy_identity_properties, add_missing_properties_left_to_right, FmcUnexpectedResponse, FmcConfigurationError
from ansible_collections.cisco.fmcansible.plugins.module_utils.fmc_swagger_client import OperationField, OperationParams, ValidationError
# from module_utils.common import HTTPMethod, equal_objects, FmcConfigurationError, FmcServerError, ResponseParams, \
#   copy_identity_properties, FmcUnexpectedResponse
# from module_utils.fmc_swagger_client import OperationField, ValidationError

DEFAULT_PAGE_SIZE = 10
DEFAULT_OFFSET = 0

BAD_REQUEST_STATUS = 400
UNPROCESSABLE_ENTITY_STATUS = 422
NOT_FOUND_STATUS = 404

NOT_EXISTS_ERROR_STR = "Referenced object does not exist"
NOT_FOUND_ERROR_MESSAGE = "Resource Not Found"
INVALID_UUID_ERROR_MESSAGE = "Validation failed due to an invalid UUID"
DUPLICATE_NAME_ERROR_MESSAGE = "Validation failed due to a duplicate name"
DUPLICATE_NAME_ERROR_STR = "already exists"

MULTIPLE_DUPLICATES_FOUND_ERROR = (
    "Multiple objects matching specified filters are found. "
    "Please, define filters more precisely to match one object exactly."
)
DUPLICATE_ERROR = (
    "Cannot add a new object. "
    "An object with the same name but different parameters already exists."
)
ADD_OPERATION_NOT_SUPPORTED_ERROR = (
    "Cannot add a new object while executing an upsert request. "
    "Creation of objects with this type is not supported."
)
BULK_UPSERT_ERROR = (
    "Cannot upsert with bulk. "
    "Upsert is only supported for single objects."
)

PATH_PARAMS_FOR_DEFAULT_OBJ = {'objId': 'default'}
PATH_IDENTITY_PARAM = 'objectId'
BULK = "bulk"
NAME = "name"
IF_NAME = "ifname"


# Note: FMC uses create/update; FTD uses add/edit
class OperationNamePrefix:
    ADD = 'add'
    CREATE = 'create'
    EDIT = 'edit'
    UPDATE = 'update'
    GET = 'get'
    DELETE = 'delete'
    UPSERT = 'upsert'


class QueryParams:
    FILTER = 'filter'


class ParamName:
    QUERY_PARAMS = 'query_params'
    PATH_PARAMS = 'path_params'
    DATA = 'data'
    FILTERS = 'filters'


class CheckModeException(Exception):
    pass


class FmcInvalidOperationNameError(Exception):
    def __init__(self, operation_name):
        super(FmcInvalidOperationNameError, self).__init__(operation_name)
        self.operation_name = operation_name


class OperationChecker(object):

    @classmethod
    def is_add_operation(cls, operation_name, operation_spec):
        """
        Check if operation defined with 'operation_name' is add object operation according to 'operation_spec'.

        :param operation_name: name of the operation being called by the user
        :type operation_name: str
        :param operation_spec: specification of the operation being called by the user
        :type operation_spec: dict
        :return: True if the called operation is add object operation, otherwise False
        :rtype: bool
        """
        # Some endpoints have non-CRUD operations, so checking operation name is required in addition to the HTTP method
        # Some op name use "add" others use "create" so support both
        return (operation_name.startswith(OperationNamePrefix.ADD) or operation_name.startswith(OperationNamePrefix.CREATE)) \
            and is_post_request(operation_spec)

    @classmethod
    def is_edit_operation(cls, operation_name, operation_spec):
        """
        Check if operation defined with 'operation_name' is edit object operation according to 'operation_spec'.

        :param operation_name: name of the operation being called by the user
        :type operation_name: str
        :param operation_spec: specification of the operation being called by the user
        :type operation_spec: dict
        :return: True if the called operation is edit object operation, otherwise False
        :rtype: bool
        """
        # Some endpoints have non-CRUD operations, so checking operation name is required in addition to the HTTP method
        # Some op name use "edit" others use "update" so support both
        return (operation_name.startswith(OperationNamePrefix.EDIT) or operation_name.startswith(OperationNamePrefix.UPDATE)) \
            and is_put_request(operation_spec)

    @classmethod
    def is_delete_operation(cls, operation_name, operation_spec):
        """
        Check if operation defined with 'operation_name' is delete object operation according to 'operation_spec'.

        :param operation_name: name of the operation being called by the user
        :type operation_name: str
        :param operation_spec: specification of the operation being called by the user
        :type operation_spec: dict
        :return: True if the called operation is delete object operation, otherwise False
        :rtype: bool
        """
        # Some endpoints have non-CRUD operations, so checking operation name is required in addition to the HTTP method
        return operation_name.startswith(OperationNamePrefix.DELETE) \
            and operation_spec[OperationField.METHOD] == HTTPMethod.DELETE

    @classmethod
    def is_get_list_operation(cls, operation_name, operation_spec):
        """
        Check if operation defined with 'operation_name' is get list of objects operation according to 'operation_spec'.

        :param operation_name: name of the operation being called by the user
        :type operation_name: str
        :param operation_spec: specification of the operation being called by the user
        :type operation_spec: dict
        :return: True if the called operation is get a list of objects operation, otherwise False
        :rtype: bool
        """
        return operation_spec[OperationField.METHOD] == HTTPMethod.GET \
            and operation_spec[OperationField.RETURN_MULTIPLE_ITEMS]

    @classmethod
    def is_get_operation(cls, operation_name, operation_spec):
        """
        Check if operation defined with 'operation_name' is get objects operation according to 'operation_spec'.

        :param operation_name: name of the operation being called by the user
        :type operation_name: str
        :param operation_spec: specification of the operation being called by the user
        :type operation_spec: dict
        :return: True if the called operation is get object operation, otherwise False
        :rtype: bool
        """
        return operation_spec[OperationField.METHOD] == HTTPMethod.GET \
            and not operation_spec[OperationField.RETURN_MULTIPLE_ITEMS]

    @classmethod
    def is_upsert_operation(cls, operation_name):
        """
        Check if operation defined with 'operation_name' is upsert objects operation according to 'operation_name'.

        :param operation_name: name of the operation being called by the user
        :type operation_name: str
        :return: True if the called operation is upsert object operation, otherwise False
        :rtype: bool
        """
        return operation_name.startswith(OperationNamePrefix.UPSERT)

    @classmethod
    def is_find_by_filter_operation(cls, operation_name, params, operation_spec):
        """
        Checks whether the called operation is 'find by filter'. This operation fetches all objects and finds
        the matching ones by the given filter. As filtering is done on the client side, this operation should be used
        only when selected filters are not implemented on the server side.

        :param operation_name: name of the operation being called by the user
        :type operation_name: str
        :param operation_spec: specification of the operation being called by the user
        :type operation_spec: dict
        :param params: params - params should contain 'filters'
        :return: True if the called operation is find by filter, otherwise False
        :rtype: bool
        """
        is_get_list = cls.is_get_list_operation(operation_name, operation_spec)
        return is_get_list and ParamName.FILTERS in params and params[ParamName.FILTERS]

    @classmethod
    def is_upsert_operation_supported(cls, operations):
        """
        Checks if all operations required for upsert object operation are defined in 'operations'.

        :param operations: specification of the operations supported by model
        :type operations: dict
        :return: True if all criteria required to provide requested called operation are satisfied, otherwise False
        :rtype: bool
        """
        has_edit_op = next((name for name, spec in iteritems(operations) if cls.is_edit_operation(name, spec)), None)
        has_get_list_op = next((name for name, spec in iteritems(operations)
                                if cls.is_get_list_operation(name, spec)), None)
        return has_edit_op and has_get_list_op


class BaseConfigurationResource(object):

    def __init__(self, conn, check_mode=False):
        self._conn = conn
        self.config_changed = False
        self._operation_spec_cache = {}
        self._models_operations_specs_cache = {}
        self._check_mode = check_mode
        self._operation_checker = OperationChecker

    def execute_operation(self, op_name, params):
        """
        Allow user request execution of simple operations(natively supported by API provider) as well as complex
        operations(operations that are implemented as a set of simple operations).

        :param op_name: name of the operation being called by the user
        :type op_name: str
        :param params: definition of the params that operation should be executed with
        :type params: dict
        :return: Result of the operation being executed
        :rtype: dict
        """
        if self._operation_checker.is_upsert_operation(op_name):
            return self.upsert_object(op_name, params)
        else:
            return self.crud_operation(op_name, params)

    def crud_operation(self, op_name, params):
        """
        Allow user request execution of simple operations(natively supported by API provider) only.

        :param op_name: name of the operation being called by the user
        :type op_name: str
        :param params: definition of the params that operation should be executed with
        :type params: dict
        :return: Result of the operation being executed
        :rtype: dict
        """
        op_spec = self.get_operation_spec(op_name)
        if op_spec is None:
            raise FmcInvalidOperationNameError(op_name)

        if self._operation_checker.is_add_operation(op_name, op_spec):
            resp = self.add_object(op_name, params)
        elif self._operation_checker.is_edit_operation(op_name, op_spec):
            resp = self.edit_object(op_name, params)
        elif self._operation_checker.is_delete_operation(op_name, op_spec):
            resp = self.delete_object(op_name, params)
        elif self._operation_checker.is_find_by_filter_operation(op_name, params, op_spec):
            resp = list(self.get_objects_by_filter(op_name, params))
        elif self._operation_checker.is_get_list_operation(op_name, op_spec):
            resp = self.list_objects(op_name, params)
        else:
            resp = self.send_general_request(op_name, params)
        return resp

    def get_operation_spec(self, operation_name):
        if operation_name not in self._operation_spec_cache:
            self._operation_spec_cache[operation_name] = self._conn.get_operation_spec(operation_name)
        return self._operation_spec_cache[operation_name]

    def get_operation_specs_by_model_name(self, model_name):
        if model_name not in self._models_operations_specs_cache:
            model_op_specs = self._conn.get_operation_specs_by_model_name(model_name)
            self._models_operations_specs_cache[model_name] = model_op_specs
            for op_name, op_spec in iteritems(model_op_specs):
                self._operation_spec_cache.setdefault(op_name, op_spec)
        return self._models_operations_specs_cache[model_name]

    def get_objects_by_filter(self, operation_name, params):
        """
        Gets a list of list objects using the specified filter params (i.e. filters: in playbook)
        """
        # filter func that filters by params, usually name
        def match_filters(obj):
            for k, v in iteritems(filter_params):
                if k not in obj or obj[k] != v:
                    return False
            return True

        filter_params = params.get(ParamName.FILTERS) or {}
        # commented out for FMC
        # unfortunately endpoints are not consistent on filter=name, and some endpoints throw an error
        # if QueryParams.FILTER not in url_params[ParamName.QUERY_PARAMS] and 'name' in filters:
        # most endpoints only support filtering by name, so remaining `filters` are applied on returned objects
        #    url_params[ParamName.QUERY_PARAMS][QueryParams.FILTER] = 'name:%s' % filters['name']

        return self.get_objects_by_filter_func(operation_name, params, match_filters)

    def get_objects_by_filter_func(self, operation_name, params, filter_func):
        # extract query and path params for list operation
        __, query_params, path_params = _get_user_params(params)
        # copy required params to avoid mutation of passed `params` dict
        url_params = {ParamName.QUERY_PARAMS: dict(query_params), ParamName.PATH_PARAMS: dict(path_params)}

        # load list items
        item_generator = iterate_over_pageable_resource(
            partial(self.send_general_request, operation_name=operation_name), url_params
        )
        return (i for i in item_generator if filter_func(i))

    def _find_existing_object(self, model_name, path_params, object_id):
        get_operation = self._find_get_operation(model_name)
        if not get_operation:
            return None
        path_params_for_find = (path_params or {}).copy()
        # only set objectId if it has a value - this is so validation will fail
        if object_id is not None:
            path_params_for_find[PATH_IDENTITY_PARAM] = object_id
        return self.send_general_request(get_operation, {ParamName.PATH_PARAMS: path_params_for_find})

    def _stringify_name_filter(self, filters):
        build_version = self.get_build_version()
        if build_version >= '6.4.0':
            return "fts~%s" % (filters['name'])
        return "name:%s" % (filters['name'])

    def _fetch_system_info(self):
        if not self._system_info:
            params = {ParamName.PATH_PARAMS: PATH_PARAMS_FOR_DEFAULT_OBJ}
            self._system_info = self.send_general_request('getSystemInformation', params)

        return self._system_info

    def get_build_version(self):
        system_info = self._fetch_system_info()
        return system_info['databaseInfo']['buildVersion']

    def is_bulk_operation(self, params):
        """
        Determines if operations is a bulk operation by checking if query param bulk=true
        and data passed is a list.
        """
        data, query_params, path_params = _get_user_params(params)
        is_bulk = query_params.get(BULK) is True
        is_data_list = isinstance(data, list)
        return is_bulk or is_data_list

    def ensure_bulk_data_params(self, params):
        """
        If operation is a bulk operation, ensures and/or converts the data into a list.
        """
        if self.is_bulk_operation(params):
            data = params[ParamName.DATA] or None
            if data is not None and not isinstance(data, list):
                params[ParamName.DATA] = [data]
        return params

    def add_object(self, operation_name, params):
        def is_duplicate_name_error(err):
            # note: FMC normally returns 400 for duplicates, but sometimes 422
            return (err.code == BAD_REQUEST_STATUS or err.code == UNPROCESSABLE_ENTITY_STATUS) \
                and (DUPLICATE_NAME_ERROR_STR in str(err) or str(err) == DUPLICATE_NAME_ERROR_MESSAGE)

        is_bulk = self.is_bulk_operation(params)
        # for bulk operation, skip equality check since there are multiple
        if is_bulk:
            params = self.ensure_bulk_data_params(params)
        else:
            # some API calls do not raise a duplicate error, so check for duplicate beforehand
            existing_obj = self._check_equality_with_existing_object(operation_name, params)
            if existing_obj is not None:
                return existing_obj

        try:
            return self.send_general_request(operation_name, params)
        except FmcServerError as e:
            if is_duplicate_name_error(e) and not self.is_bulk_operation(params):
                # only support equality check in non-bulk scenario
                existing_obj = self._check_equality_with_existing_object(operation_name, params)
                if existing_obj is None:
                    raise e
            else:
                raise e

    def _check_equality_with_existing_object(self, operation_name, params):
        """
        Looks for an existing object that caused "object duplicate" error and
        checks whether it corresponds to the one specified in `params`.

        In case a single object is found and it is equal to one we are trying
        to create, the existing object is returned.

        When the existing object is not equal to the object being created or
        several objects are returned, an exception is raised.

        For FMC, this function only supports checking against a single object.
        """
        model_name = self.get_operation_spec(operation_name).get(OperationField.MODEL_NAME)
        # get list object first - this only contains id, name, type
        existing_list_obj = self._find_object_matching_params(model_name, params)

        if existing_list_obj is not None:
            # get full existing object
            playbook_obj = params[ParamName.DATA]
            existing_obj = self._find_existing_object(model_name, params[ParamName.PATH_PARAMS], existing_list_obj['id'])
            model = self._conn.get_model_spec(model_name)
            if is_playbook_obj_equal_to_api_obj(playbook_obj, existing_obj, model):
                return existing_obj
            else:
                raise FmcConfigurationError(DUPLICATE_ERROR, existing_obj)

        return None

    def _find_object_matching_params(self, model_name, params):
        """
        Attempts to find existing, equivalent objects matching the parameters
        Returns the existing objects if it exists, or None if not found.
        """
        def compare_whole_object(obj):
            if 'id' not in obj:
                return False
            existing_obj = self._find_existing_object(model_name, params[ParamName.PATH_PARAMS], obj['id'])
            return is_playbook_obj_equal_to_api_obj(data, existing_obj, model)

        def filter_on_name_or_whole_object(obj):
            # if model contains ifname, compare both objects on that
            if use_if_name:
                if obj.get(IF_NAME) is not None and data.get(IF_NAME) is not None:
                    return data.get(IF_NAME) == obj.get(IF_NAME)
                else:
                    return compare_whole_object(obj)
            else:
                # if no name provided on either client or server object, must match whole object
                if obj.get(NAME) is None or data_name is None:
                    return compare_whole_object(obj)
                elif obj[NAME] == data_name:
                    return True
            return False

        get_list_operation = self._find_get_list_operation(model_name)
        if not get_list_operation:
            return None

        data = params[ParamName.DATA]
        # some objects is 'ifname' as unique name
        data_name = data.get(NAME)
        model = self._conn.get_model_spec(model_name)
        use_if_name = model_has_property(model, IF_NAME)

        obj = None
        filtered_objs = self.get_objects_by_filter_func(get_list_operation, params, filter_on_name_or_whole_object)

        for i, obj in enumerate(filtered_objs):
            if i > 0:
                raise FmcConfigurationError(MULTIPLE_DUPLICATES_FOUND_ERROR)
            obj = obj

        return obj

    def _find_get_list_operation(self, model_name):
        operations = self.get_operation_specs_by_model_name(model_name) or {}
        return next((
            op for op, op_spec in operations.items()
            if self._operation_checker.is_get_list_operation(op, op_spec)), None)

    def _find_get_operation(self, model_name):
        operations = self.get_operation_specs_by_model_name(model_name) or {}
        return next((
            op for op, op_spec in operations.items()
            if self._operation_checker.is_get_operation(op, op_spec)), None)

    def delete_object(self, operation_name, params):
        def is_not_found_error(err):
            # note: FMC normally returns 404 for not found
            return err.code == NOT_FOUND_STATUS or NOT_FOUND_ERROR_MESSAGE in str(err)

        try:
            return self.send_general_request(operation_name, params)
        except FmcServerError as e:
            if is_not_found_error(e):
                return {'status': NOT_EXISTS_ERROR_STR}
            else:
                raise e

    def edit_object(self, operation_name, params):
        data, __, path_params = _get_user_params(params)
        is_bulk = self.is_bulk_operation(params)

        # for bulk operation, skip equality check since there are multiple
        if is_bulk:
            params = self.ensure_bulk_data_params(params)
            return self.send_general_request(operation_name, params)

        # normalize id between path_params and data.id (path params takes precedence)
        object_id = path_params.get(PATH_IDENTITY_PARAM)
        if data is not None:
            data['id'] = object_id

        # lookup get operation to check equality
        model_name = self.get_operation_spec(operation_name)[OperationField.MODEL_NAME]
        model = self._conn.get_model_spec(model_name)
        existing_object = self._find_existing_object(model_name, path_params, object_id)
        if not existing_object:
            raise FmcConfigurationError(NOT_EXISTS_ERROR_STR)
        elif is_playbook_obj_equal_to_api_obj(data, existing_object, model):
            return existing_object

        return self.send_general_request(operation_name, params)

    def list_objects(self, operation_name, params):
        """
        Executes a "get all" operation and normalizes the list.
        """
        list_obj = self.send_general_request(operation_name, params)
        if list_obj is None:
            return list_obj
        if list_obj.get('items') is None:
            list_obj['items'] = []
        return list_obj

    def send_general_request(self, operation_name, params):
        def stop_if_check_mode():
            if self._check_mode:
                raise CheckModeException()

        self.validate_params(operation_name, params)
        stop_if_check_mode()

        data, query_params, path_params = _get_user_params(params)
        op_spec = self.get_operation_spec(operation_name)

        filtered_query_params = {}
        for key, val in query_params.items():
            if key in op_spec[OperationField.PARAMETERS][OperationParams.QUERY].keys():
                filtered_query_params[key] = val
        
        url, method = op_spec[OperationField.URL], op_spec[OperationField.METHOD]

        return self._send_request(url, method, data, path_params, filtered_query_params)

    def _send_request(self, url_path, http_method, body_params=None, path_params=None, query_params=None):
        def raise_for_failure(resp):
            if not resp[ResponseParams.SUCCESS]:
                raise FmcServerError(resp[ResponseParams.RESPONSE], resp[ResponseParams.STATUS_CODE])

        response = self._conn.send_request(url_path=url_path, http_method=http_method, body_params=body_params,
                                           path_params=path_params, query_params=query_params)
        raise_for_failure(response)
        if http_method != HTTPMethod.GET:
            self.config_changed = True
        return response[ResponseParams.RESPONSE]

    def validate_params(self, operation_name, params):
        report = {}
        op_spec = self.get_operation_spec(operation_name)
        data, query_params, path_params = _get_user_params(params)

        def validate(validation_method, field_name, user_params):
            key = 'Invalid %s provided' % field_name
            try:
                is_valid, validation_report = validation_method(operation_name, user_params)
                if not is_valid:
                    report[key] = validation_report
            except Exception as e:
                report[key] = str(e)
            return report

        validate(self._conn.validate_query_params, ParamName.QUERY_PARAMS, query_params)
        validate(self._conn.validate_path_params, ParamName.PATH_PARAMS, path_params)
        if is_post_request(op_spec) or is_put_request(op_spec):
            validate(self._conn.validate_data, ParamName.DATA, data)

        if report:
            raise ValidationError(report)

    @staticmethod
    def _get_operation_name(checker, operations):
        return next((op_name for op_name, op_spec in iteritems(operations) if checker(op_name, op_spec)), None)

    def _add_upserted_object(self, model_operations, params):
        add_op_name = self._get_operation_name(self._operation_checker.is_add_operation, model_operations)
        if not add_op_name:
            raise FmcConfigurationError(ADD_OPERATION_NOT_SUPPORTED_ERROR)
        return self.add_object(add_op_name, params)

    def _edit_upserted_object(self, model_operations, existing_object, params):
        edit_op_name = self._get_operation_name(self._is_upsertable_edit_operation, model_operations)
        _set_default(params, ParamName.PATH_PARAMS, {})
        _set_default(params, ParamName.DATA, {})

        # note FMC uses objectId, FTD uses objId
        params[ParamName.PATH_PARAMS][PATH_IDENTITY_PARAM] = existing_object['id']
        copy_identity_properties(existing_object, params[ParamName.DATA])

        return self.edit_object(edit_op_name, params)

    def _is_upsertable_edit_operation(self, operation_name, operation_spec):
        """
        Determines if the edit operation begins with 'edit' or 'update', and contains
        the identity param (i.e. objectId) in its url path
        """
        return self._operation_checker.is_edit_operation(operation_name, operation_spec) and \
            (operation_spec.get(OperationField.PARAMETERS) is None or
             operation_spec[OperationField.PARAMETERS]['path'].get(PATH_IDENTITY_PARAM) is not None)

    def upsert_object(self, op_name, params):
        """
        Updates an object if it already exists, or tries to create a new one if there is no
        such object. If multiple objects match filter criteria, or add operation is not supported,
        the exception is raised.

        :param op_name: upsert operation name
        :type op_name: str
        :param params: params that upsert operation should be executed with
        :type params: dict
        :return: upserted object representation
        :rtype: dict
        """

        # strips the model name from op name (i.e. upsertAccessPolicy -> AccessPolicy)
        def extract_and_validate_model():
            model = op_name[len(OperationNamePrefix.UPSERT):]
            if not self._conn.get_model_spec(model):
                raise FmcInvalidOperationNameError(op_name)
            return model

        model_name = extract_and_validate_model()
        model_operations = self.get_operation_specs_by_model_name(model_name)

        if not self._operation_checker.is_upsert_operation_supported(model_operations):
            raise FmcInvalidOperationNameError(op_name)

        # ensure that bulk data was not passed
        if self.is_bulk_operation(params):
            raise FmcConfigurationError(BULK_UPSERT_ERROR)

        # retrieve object via list operation, create or update it
        existing_obj = self._find_object_matching_params(model_name, params)
        if existing_obj:
            # equal_to_existing_obj = equal_objects(existing_obj, params[ParamName.DATA])
            # return existing_obj if equal_to_existing_obj \
            #    else self._edit_upserted_object(model_operations, existing_obj, params)
            # Note: for FMC we cannot check equality here because the list operation just returns name and type
            # edit_object will do a deeper equality check on the exact object
            return self._edit_upserted_object(model_operations, existing_obj, params)
        else:
            return self._add_upserted_object(model_operations, params)


def _set_default(params, field_name, value):
    if field_name not in params or params[field_name] is None:
        params[field_name] = value


def is_post_request(operation_spec):
    return operation_spec[OperationField.METHOD] == HTTPMethod.POST


def is_put_request(operation_spec):
    return operation_spec[OperationField.METHOD] == HTTPMethod.PUT


def _get_user_params(params):
    return params.get(ParamName.DATA) or {}, params.get(ParamName.QUERY_PARAMS) or {}, params.get(
        ParamName.PATH_PARAMS) or {}


def iterate_over_pageable_resource(resource_func, params):
    """
    A generator function that iterates over a resource that supports pagination and lazily returns present items
    one by one.

    :param resource_func: function that receives `params` argument and returns a page of objects
    :type resource_func: callable
    :param params: initial dictionary of parameters that will be passed to the resource_func.
                   Should contain `query_params` inside.
    :type params: dict
    :return: an iterator containing returned items
    :rtype: iterator of dict
    """
    # creating a copy not to mutate passed dict
    params = copy.deepcopy(params)
    params[ParamName.QUERY_PARAMS].setdefault('limit', DEFAULT_PAGE_SIZE)
    params[ParamName.QUERY_PARAMS].setdefault('offset', DEFAULT_OFFSET)
    limit = int(params[ParamName.QUERY_PARAMS]['limit'])

    def received_less_items_than_requested(items_in_response, items_expected):
        if items_in_response == items_expected:
            return False
        elif items_in_response < items_expected:
            return True

        raise FmcUnexpectedResponse(
            "Get List of Objects Response from the server contains more objects than requested. "
            "There are {0} item(s) in the response while {1} was(ere) requested".format(
                items_in_response, items_expected)
        )

    while True:
        result = resource_func(params=params)
        items = result.get('items')

        # When there are no items, FMC sometimes omits the property completely
        if items is None:
            break

        for item in items:
            yield item

        if received_less_items_than_requested(len(items), limit):
            break

        # creating a copy not to mutate existing dict
        params = copy.deepcopy(params)
        query_params = params[ParamName.QUERY_PARAMS]
        query_params['offset'] = int(query_params['offset']) + limit


def model_has_property(model, prop_name):
    """
    Gets whether the model spec object contains the specified property name.
    """
    return model and type(model) == dict and model.get('properties') is not None and model.get('properties').get(prop_name) is not None


def is_playbook_obj_equal_to_api_obj(obj_client, obj_server, model=None):
    """
    Wrapper call to equal_objects(), strips type from obj1 first since type names will be slightly different
    based on origin from FMC API.
    If model is passed (from API spec), will also sanitize both objects to ensure only properties in the model are compared.
    """
    # clone objects
    d1 = dict(obj_client)
    d2 = dict(obj_server)
    # remove properties not in model
    # this prevents comparison fails due to misspelled/invalid properties used in playbook
    if model and model.get("properties"):
        # remove properties from obj_client not in model
        d1 = delete_props_not_in_model(d1, model)
        # remove properties from obj_client not in model (note: this should never happen but check to be sure)
        d2 = delete_props_not_in_model(d2, model)
    # copy missing properties to d2, to compare using additive approach
    add_missing_properties_left_to_right(d1, d2)
    # because FMC can be inconsistent on type name, remove from source dict for comparison
    return equal_objects(d1, d2)
