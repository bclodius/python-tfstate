# -*- coding: utf-8 -*-

# Python stdlib
import json

# tfstate
from tfstate.base.module import Module


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
