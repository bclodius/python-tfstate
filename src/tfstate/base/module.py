# -*- coding: utf-8 -*-

# tfstate
from tfstate.base.resource import Resource


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

        self.parse_resource_relations()

    @staticmethod
    def load_list(module_list):
        """
        Parse the list of native modules into a list of Module objects

        :param list module_list: Native module list
        :returns: List of Module
        :rtype: list
        """

        return [Module(module) for module in module_list]

    def parse_resource_relations(self):
        """
        Parse the resource dependencies and adds its relations
        """

        for resource_name, resource_object in self.resources.items():
            for relation_name in resource_object.dependencies:
                relation_object = self.resources[relation_name]
                resource_object.relations[relation_name] = relation_object
