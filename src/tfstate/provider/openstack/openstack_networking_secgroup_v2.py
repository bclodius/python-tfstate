# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.openstack import OpenStackResource
from tfstate.exceptions import InvalidResource


class OSNetworkingSecgroupV2(OpenStackResource):
    """
    Provides an OpenStack V2 Networking Security Group.

    Usage::

        OSNetworkingSecgroupV2(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "openstack_networking_secgroup_v2":
            raise InvalidResource(
                "OSNetworkingSecgroupV2 must be of 'openstack_networking_secgroup_v2' type")
        attributes = self.primary_data['attributes']
        self.description = attributes.get('description', None)
        self.name = attributes.get('name', None)
        self.tenant_id = attributes.get('tenant_id', None)
