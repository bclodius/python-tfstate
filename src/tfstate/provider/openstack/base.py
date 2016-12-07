# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.base import Resource


class OpenStackResource(Resource):
    """
    Class to represent an OpenStack provided resource

    Usage::

        OpenStackResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        self.terraform_provider = "openstack"
