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

        Tfstate(file_descriptor)
    """

    def __init__(self, file_descriptor):
        """
        :param file file_descriptor: tfstate file descriptor
        """

        self.tfstate_file = file_descriptor
        self.load_tfstate_data_from_file()
        self.version = self.native_data.get('version', None)
        self.serial = self.native_data.get('serial', None)
        self.terraform_version = self.native_data.get('terraform_version', None)
        self.lineage = self.native_data.get('lineage', None)
        self.modules = Module.load_list(self.native_data.get('modules', []))

    def load_tfstate_data_from_file(self):
        """
        Read the tfstate file and load its contents, parses then as JSON and put the result into the object
        """
        self.tfstate_file.seek(0)
        tfstate_data = self.tfstate_file.read()
        if isinstance(tfstate_data, bytes):
            tfstate_data = tfstate_data.decode('utf-8')
        self.native_data = json.loads(tfstate_data)
