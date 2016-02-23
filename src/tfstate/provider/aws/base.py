# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.base import Resource


class AwsResource(Resource):
    """
    Class to represent an AWS provided resource

    Usage::

        AwsResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        self.provider = "aws"
        self.id = self.primary_data['id']
