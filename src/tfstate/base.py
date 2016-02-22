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
        self.modules = TfstateModule.load_modules_list(self.native_data.get('modules'))

    def load_tfstate_data_from_file(self):
        """
        Read the tfstate file and load its contents, parses then as JSON and put the result into the object
        """

        tfstate_file = open(self.tfstate_path, 'r')
        self.native_data = json.load(tfstate_file)


class TfstateModule(object):
    """
    Class to represent a module object from a tfstate file

    Usage::

        TfstateModule(native_data)
    """

    def __eq__(self, other):
        return self.native_data == other.native_data

    def __init__(self, native_data):
        """
        :param dict native_data: Module native data to parse
        """

        self.native_data = native_data

    @staticmethod
    def load_modules_list(module_list):
        """
        Parse the list of native modules into a list of TfstateModule objects

        :param list module_list: Native module list
        :returns: List of TfstateModule
        :rtype: list
        """

        object_list = [TfstateModule(module) for module in module_list]
        return object_list
