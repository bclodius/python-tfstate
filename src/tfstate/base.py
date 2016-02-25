# -*- coding: utf-8 -*-

# Python stdlib
import json


class Tfstate(object):
    """
    Base tfstate object class
    Load tfstate file and parses it

    Usage::

        Tfstate(file_path)
    """

    def __init__(self, file_path):
        """
        :param str file_path: tfstate file path
        """

        self.tfstate_path = file_path
        self.load_tfstate_data_from_file()
        self.version = self.native_data.get('version', None)
        self.serial = self.native_data.get('serial', None)
        self.modules = Module.load_list(self.native_data.get('modules'))

    def load_tfstate_data_from_file(self):
        """
        Read the tfstate file and load its contents, parses then as JSON and put the result into the object
        """

        tfstate_file = open(self.tfstate_path, 'r')
        self.native_data = json.load(tfstate_file)


class Module(object):
    """
    Class to represent a module object from a tfstate file

    Usage::

        Module(native_data)
    """

    def __eq__(self, other):
        return self.native_data == other.native_data

    def __init__(self, native_data):
        """
        :param dict native_data: Module native data to parse
        """

        self.native_data = native_data
        self.path = self.native_data.get('path', None)
        self.outputs = self.native_data.get('outputs', None)
        self.resources = Resource.load_dict(self.native_data.get('resources', {}))

    @staticmethod
    def load_list(module_list):
        """
        Parse the list of native modules into a list of Module objects

        :param list module_list: Native module list
        :returns: List of Module
        :rtype: list
        """

        return [Module(module) for module in module_list]


class Resource(object):
    """
    Class to represent a resource from a tfstate file

    Usage::

        Resource(resource_name, native_data)
    """

    def __eq__(self, other):
        name = self.resource_name == other.resource_name
        native_data = self.native_data == other.native_data
        return name and native_data

    def __init__(self, resource_name, native_data):
        self.provider = None
        self.native_data = native_data
        self.resource_name = resource_name
        self.resource_type = self.native_data.get('type', None)
        self.dependencies = self.native_data.get('depends_on', [])
        self.primary_data = self.native_data.get('primary', {})
        self.parse_compound_attributes()

    @staticmethod
    def _parse_nested_parameters(name_list, value):
        nested_name = name_list[0]
        if len(name_list) > 1:
            nested_value = Resource._parse_nested_parameters(name_list[1:], value)
        else:
            if value == 'true':
                value = True
            elif value == 'false':
                value = False
            nested_value = value

        return {nested_name: nested_value}

    @staticmethod
    def _extend_nested_directory(parent_dict, line_dict):
        name, value = line_dict.popitem()
        parent_value = parent_dict.get(name, None)
        if parent_value is None:
            parent_dict[name] = value
        else:
            parent_dict[name] = Resource._extend_nested_directory(parent_value, value)

        return parent_dict

    def parse_compound_attributes(self):
        parsed_dict = {}
        for name, value in self.primary_data['attributes'].items():
            name_list = name.split('.')
            if len(name_list) > 1 and name_list[len(name_list)-1] != '#':
                parsed_line = Resource._parse_nested_parameters(name_list, value)
                parsed_dict = Resource._extend_nested_directory(parsed_dict, parsed_line)
        self.compound_attributes = parsed_dict

    def get_boolean_attribute(self, attribute):
        """
        Parse a boolean attribute to a native python boolean

        :param str attribute: Parse the attribute given
        """

        attributes = self.primary_data['attributes']
        value = attributes.get(attribute, None)
        if value is None:
            raise AttributeError('Attribute {} does not exist'.format(attribute))
        else:
            return True if value == 'true' else False

    @staticmethod
    def load_dict(resources_dict):
        """
        Parse the list of native modules into a list of Module objects

        :param list module_list: Native module list
        :returns: List of Module
        :rtype: list
        """

        return {name: Resource(name, data) for name, data in resources_dict.items()}
