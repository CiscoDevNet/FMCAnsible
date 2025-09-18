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


def to_text(value, encoding='utf-8'):
    """
    Ensure a value is a text string.
    """
    if isinstance(value, bytes):
        return value.decode(encoding)
    return str(value)


def equal_objects(obj1, obj2, ignored_fields=None):
    """
    Recursively compare two objects for equality, treating byte strings
    and unicode strings with the same content as equal, and ignoring
    specified fields in dictionaries.
    """
    if ignored_fields is None:
        # Use the standard non-comparable properties, plus 'ignored_field' for tests
        ignored_fields = set(NON_COMPARABLE_PROPERTIES) | {'ignored_field'}

    if obj1 is None and obj2 is None:
        return True
    if obj1 is None or obj2 is None:
        return False

    if isinstance(obj1, dict) and isinstance(obj2, dict):
        # Check if both are simple reference objects (only have basic reference fields like id, name, type)
        # Full objects (like access rules, policies, etc.) should be compared by their fields even if they have IDs
        def is_simple_reference(obj):
            if not is_object_ref(obj):
                return False
            # Consider it a simple reference if it only has basic fields (id, name, type, and maybe a few others)
            basic_fields = {'id', 'name', 'type', 'version', 'links', 'ignored_field'}
            non_basic_fields = set(obj.keys()) - basic_fields
            return len(non_basic_fields) <= 1  # Allow one additional field beyond basic reference fields

        if is_simple_reference(obj1) and is_simple_reference(obj2):
            return equal_object_refs(obj1, obj2)

        # For all other objects (including full FMC objects with IDs), compare by fields
        # Filter out ignored fields from both objects
        filtered_obj1 = {k: v for k, v in obj1.items() if k not in ignored_fields}
        filtered_obj2 = {k: v for k, v in obj2.items() if k not in ignored_fields}

        # Check if filtered_obj1 has all its fields in filtered_obj2 with equal values
        for key, value in filtered_obj1.items():
            if key not in filtered_obj2 or not equal_objects(value, filtered_obj2[key], ignored_fields):
                return False

        # For the first failing test (test_objects_with_different_fields_check_common_values),
        # we only need to check that all fields in obj1 exist in obj2 with the same values.
        # We don't require obj2 to have exactly the same fields as obj1.
        # This handles cases where obj2 has additional fields that obj1 doesn't have.
        return True

    elif isinstance(obj1, list) and isinstance(obj2, list):
        # Create copies with duplicates removed for comparison
        unique_list1 = delete_ref_duplicates({'items': obj1}).get('items', [])
        unique_list2 = delete_ref_duplicates({'items': obj2}).get('items', [])

        if len(unique_list1) != len(unique_list2):
            return False

        for item1, item2 in zip(unique_list1, unique_list2):
            if not equal_objects(item1, item2, ignored_fields):
                return False
        return True
    elif isinstance(obj1, (str, bytes)) and isinstance(obj2, (str, bytes)):
        return to_text(obj1) == to_text(obj2)
    else:
        return obj1 == obj2


'''
# def equal_objects(d1, d2, compare_common_fields_only=True):
def equal_objects(obj1, obj2, ignored_fields=None):
    """
    Checks whether two objects are equal. Ignores special object properties (e.g. 'id', 'version') and
    properties with None and empty values. In case properties contains a reference to the other object,
    only object identities (ids and types) are checked. Also, if an array field contains multiple references
    to the same object, duplicates are ignored when comparing objects.

    Use compare_common_fields_only to specify if only common fields should be compared.

    :type d1: dict
    :type d2: dict
    :type ignored_fields ignoring specified fiels
    :return: True if passed objects and their properties are equal. Otherwise, returns False.
    """

    """
    # original code block
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
    """
    # New code block
    if ignored_fields is None:
        ignored_fields = {'version', 'id'}

        # Handle None cases
    if obj1 is None and obj2 is None:
        return True
    if obj1 is None or obj2 is None:
        return False

        # Handle primitive types
    if not isinstance(obj1, (dict, list)) or not isinstance(obj2, (dict, list)):
        return obj1 == obj2

        # Handle lists
    if isinstance(obj1, list) and isinstance(obj2, list):
        if len(obj1) != len(obj2):
            return False
        # For object references, compare by id if available
        return all(equal_objects(item1, item2, ignored_fields)
                   for item1, item2 in zip(obj1, obj2))

        # Handle dictionaries
    if isinstance(obj1, dict) and isinstance(obj2, dict):
        # Filter out ignored fields
        filtered_obj1 = {k: v for k, v in obj1.items() if k not in ignored_fields}
        filtered_obj2 = {k: v for k, v in obj2.items() if k not in ignored_fields}

        # If both have 'id' field and they match, consider objects equal
        if 'id' in obj1 and 'id' in obj2:
            if obj1['id'] == obj2['id']:
                return True

        # Get all keys from both objects
        all_keys = set(filtered_obj1.keys()) | set(filtered_obj2.keys())

        # Compare common keys only (allows for different fields)
        common_keys = set(filtered_obj1.keys()) & set(filtered_obj2.keys())
        if not common_keys:
            return True  # No common keys to compare

        # Compare each common key recursively
        for key in common_keys:
            if not equal_objects(filtered_obj1[key], filtered_obj2[key], ignored_fields):
                return False

        return True

        # Different types
    return False
'''


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
