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
        name = self.name == other.name
        native_data = self.native_data == other.native_data
        return name and native_data

    def __init__(self, resource_name, native_data):
        self.provider = None
        self.native_data = native_data
        self.name = resource_name
        self.resource_type = self.native_data.get('type', None)
        self.dependencies = self.native_data.get('depends_on', [])
        self.primary_data = self.native_data.get('primary', {})

    @staticmethod
    def load_dict(resources_dict):
        """
        Parse the list of native modules into a list of Module objects

        :param list module_list: Native module list
        :returns: List of Module
        :rtype: list
        """

        return {name: Resource(name, data) for name, data in resources_dict.items()}
