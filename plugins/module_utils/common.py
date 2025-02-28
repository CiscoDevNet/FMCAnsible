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

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import re
from ansible.module_utils._text import to_text
from ansible.module_utils.common.collections import is_string


INVALID_IDENTIFIER_SYMBOLS = r'[^a-zA-Z0-9_]'

IDENTITY_PROPERTIES = ['id', 'version', 'ruleId']
NON_COMPARABLE_PROPERTIES = IDENTITY_PROPERTIES + ['isSystemDefined', 'links', 'token', 'metadata', 'type']


class HTTPMethod:
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    DELETE = 'delete'


class ResponseParams:
    SUCCESS = 'success'
    STATUS_CODE = 'status_code'
    RESPONSE = 'response'


class FmcConfigurationError(Exception):
    def __init__(self, msg, obj=None):
        super(FmcConfigurationError, self).__init__(msg)
        self.msg = msg
        self.obj = obj


class FmcServerError(Exception):
    def __init__(self, response, code):
        super(FmcServerError, self).__init__(response)
        self.response = response
        self.code = code


class FmcUnexpectedResponse(Exception):
    """The exception to be raised in case of unexpected responses from 3d parties."""
    pass


def construct_ansible_facts(response, params):
    facts = dict()
    if response:
        response_body = response['items'] if 'items' in response else response
        if params.get('register_as'):
            facts[params['register_as']] = response_body
        # meignw2021
        # elif response_body.get('name') and response_body.get('type'):
        elif isinstance(response_body, dict) and response_body.get('name') and response_body.get('type'):
            object_name = re.sub(INVALID_IDENTIFIER_SYMBOLS, '_', response_body['name'].lower())
            fact_name = '%s_%s' % (response_body['type'], object_name)
            facts[fact_name] = response_body
    return facts


def copy_identity_properties(source_obj, dest_obj):
    for property_name in IDENTITY_PROPERTIES:
        if property_name in source_obj:
            dest_obj[property_name] = source_obj[property_name]
    return dest_obj


def is_object_ref(d):
    """
    Checks if a dictionary is a reference object. The dictionary is considered to be a
    reference object when it contains non-empty 'id' and 'type' fields.

    :type d: dict
    :return: True if passed dictionary is a reference object, otherwise False
    """
    has_id = 'id' in d.keys() and d['id']
    return has_id
    # commented out, types may not match between client and server due to formatting
    # id is sufficient to compare
    # has_id = 'id' in d.keys() and d['id']
    # has_type = 'type' in d.keys() and d['type']
    # return has_id # and has_type


def equal_object_refs(d1, d2):
    """
    Checks whether two references point to the same object.

    :type d1: dict
    :type d2: dict
    :return: True if passed references point to the same object, otherwise False
    """
    # compare by type not supported, see is_object_ref()
    have_equal_ids = d1.get('id') == d2.get('id')
    # have_equal_names = d1.get('name') == d2.get('name')
    return have_equal_ids
    # have_equal_types = d1['type'] == d2['type']


def equal_lists(l1, l2):
    """
    Checks whether two lists are equal. The order of elements in the arrays is important.

    :type l1: list
    :type l2: list
    :return: True if passed lists, their elements and order of elements are equal. Otherwise, returns False.
    """
    if len(l1) != len(l2):
        return False

    for v1, v2 in zip(l1, l2):
        if not equal_values(v1, v2):
            return False

    return True


def equal_dicts(d1, d2, compare_by_reference=True):
    """
    Checks whether two dictionaries are equal. If `compare_by_reference` is set to True, dictionaries referencing
    objects are compared using `equal_object_refs` method. Otherwise, every key and value is checked.

    :type d1: dict
    :type d2: dict
    :param compare_by_reference: if True, dictionaries referencing objects are compared using `equal_object_refs` method
    :return: True if passed dicts are equal. Otherwise, returns False.
    """
    if compare_by_reference:
        if is_object_ref(d1) and is_object_ref(d2):
            return equal_object_refs(d1, d2)
        elif is_object_ref(d2):
            # if right side (from server) has id but not left side, compare common properties only
            return equal_objects(d1, d2, True)

    if len(d1) != len(d2):
        return False

    for key, v1 in d1.items():
        if key not in d2:
            return False

        v2 = d2[key]
        if not equal_values(v1, v2):
            return False

    return True


def equal_values(v1, v2):
    """
    Checks whether types and content of two values are the same. In case of complex objects, the method might be
    called recursively.

    :param v1: first value
    :param v2: second value
    :return: True if types and content of passed values are equal. Otherwise, returns False.
    :rtype: bool
    """

    # string-like values might have same text but different types, so checking them separately
    if is_string(v1) and is_string(v2):
        return to_text(v1) == to_text(v2)

    # if type(v1) != type(v2):
    if isinstance(v1, type(v2)):
        return False
    value_type = type(v1)

    if value_type == list:
        return equal_lists(v1, v2)
    elif value_type == dict:
        return equal_dicts(v1, v2)
    else:
        return v1 == v2


def equal_objects(d1, d2, compare_common_fields_only=True):
    """
    Checks whether two objects are equal. Ignores special object properties (e.g. 'id', 'version') and
    properties with None and empty values. In case properties contains a reference to the other object,
    only object identities (ids and types) are checked. Also, if an array field contains multiple references
    to the same object, duplicates are ignored when comparing objects.

    Use compare_common_fields_only to specify if only common fields should be compared.

    :type d1: dict
    :type d2: dict
    :type compare_common_fields_only: bool
    :return: True if passed objects and their properties are equal. Otherwise, returns False.
    """

    def prepare_data_for_comparison(d, keys):
        d = dict((k, v) for k, v in d.items() if k not in NON_COMPARABLE_PROPERTIES and v)
        d = delete_ref_duplicates(d)

        if keys:
            d = dict((k, v) for k, v in d.items() if k in keys)

        return d

    common_keys = set(d1.keys()) & set(d2.keys()) if compare_common_fields_only else None

    d1 = prepare_data_for_comparison(d1, common_keys)
    d2 = prepare_data_for_comparison(d2, common_keys)
    return equal_dicts(d1, d2, compare_by_reference=False)


def add_missing_properties_left_to_right(d1, d2):
    """
    Checks whether two objects are equal using the additive approach. This means that d1 can contain less
    properties than d2, but not vice versa. Similar to equal_objects() except compare_common_fields_only
    true for the left side (d2) only.

    :type d1: dict
    :type d2: dict
    :return: True if passed objects and their properties are equal. Otherwise, returns False.
    """
    additive_keys = d1.keys()
    d2_keys = d2.keys()
    # d2 = dict(d2)
    # copy empty values to right side recursively before comparison
    # this will force equal_objects() to false if left side has more properties
    for key in additive_keys:
        if key not in d2_keys:
            # special case: name - if in d1 and not in d2, then ignore (set d2 so they match)
            if key == "name":
                new_obj = d1[key]
            else:
                new_obj = empty_value(d1[key])
            d2[key] = new_obj
        # elif type(d1[key]) == dict and type(d2[key]) == dict:
        elif isinstance(d1[key], dict) and isinstance(d2[key], dict):
            add_missing_properties_left_to_right(d1[key], d2[key])


def empty_value(val):
    """
    Returns an empty value for specified value i.e. [], {} or None
    """
    value_type = type(val)
    if value_type == list:
        return []
    elif value_type == dict:
        return {}
    elif val is None:
        return None
    else:
        return 0


def delete_ref_duplicates(d):
    """
    Removes reference duplicates from array fields: if an array contains multiple items and some of
    them refer to the same object, only unique references are preserved (duplicates are removed).

    :param d: dict with data
    :type d: dict
    :return: dict without reference duplicates
    """

    def delete_ref_duplicates_from_list(refs):
        # if all(type(i) == dict and is_object_ref(i) for i in refs):
        if all(isinstance(i, dict) and is_object_ref(i) for i in refs):
            unique_reference_map = OrderedDict()
            for i in refs:
                # some nested objects do not include type, so supply fallback value just in case
                obj_type = i.get('type') or 'Unknown'
                unique_key = (i['id'], obj_type)
                unique_reference_map[unique_key] = i
            return list(unique_reference_map.values())
        else:
            return refs

    if not d:
        return d

    modified_d = {}
    # meignw2021
    # for k, v in iteritems(d):
    for k, v in d.items():
        # if type(v) == list:
        if isinstance(v, list):
            modified_d[k] = delete_ref_duplicates_from_list(v)
        # elif type(v) == dict:
        elif isinstance(v, dict):
            modified_d[k] = delete_ref_duplicates(v)
        else:
            modified_d[k] = v
    return modified_d


def delete_props_not_in_model(obj, model):
    """
    Deletes properties from an object that do not match its corresponding model
    """
    obj_to_check = dict(obj)
    # remove properties from obj_client not in model
    props = model.get("properties")
    if props is None:
        return obj
    for key in obj:
        if key not in props:
            del obj_to_check[key]
    return obj_to_check
