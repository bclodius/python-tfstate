# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.base import Resource
from tfstate.exceptions import InvalidResource


class NullDataSource(Resource):
    """
    The null_resource is a resource that allows you to configure provisioners
    that are not directly associated with a single existing resource.

    Usage::

        NullDataSource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "null_data_source":
            raise InvalidResource("NullDataSource must be of 'null_data_source' type")
