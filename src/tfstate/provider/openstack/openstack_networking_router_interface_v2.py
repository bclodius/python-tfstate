# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.openstack import OpenStackResource
from tfstate.exceptions import InvalidResource


class OSNetworkingRouterInterfaceV2(OpenStackResource):
    """
    Provides an OpenStack V2 Networking Router Interface.

    Usage::

        OSNetworkingRouterInterfaceV2(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "openstack_networking_router_interface_v2":
            raise InvalidResource(
                "OSNetworkingRouterInterfaceV2 must be of 'openstack_networking_router_interface_v2' type")
        attributes = self.primary_data['attributes']
        self.router_id = attributes.get('router_id', None)
        self.subnet_id = attributes.get('subnet_id', None)
