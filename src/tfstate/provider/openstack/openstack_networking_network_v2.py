# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.openstack import OpenStackResource
from tfstate.exceptions import InvalidResource


class OSNetworkingNetworkV2(OpenStackResource):
    """
    Provides an OpenStack V2 Networking Network.

    Usage::

        OSNetworkingNetworkV2(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "openstack_networking_network_v2":
            raise InvalidResource(
                "OSNetworkingNetworkV2 must be of 'openstack_networking_network_v2' type")
        attributes = self.primary_data['attributes']
        self.name = attributes.get('name', None)
        self.tenant_id = attributes.get('tenant_id', None)
        self.admin_state_up = self.get_boolean_attribute('admin_state_up')
        self.shared = self.get_boolean_attribute('shared')
