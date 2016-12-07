# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.openstack import OpenStackResource
from tfstate.exceptions import InvalidResource


class OSComputeFloatingIPV2(OpenStackResource):
    """
    Provides an OpenStack V2 Compute Floating IP

    Usage::

        OSComputeFloatingIPV2(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "openstack_compute_floatingip_v2":
            raise InvalidResource(
                "OSComputeFloatingIPV2 must be of 'openstack_compute_floatingip_v2' type")
        attributes = self.primary_data['attributes']
        self.address = attributes.get('address', None)
        self.fixed_ip = attributes.get('fixed_ip', None)
        self.instance_id = attributes.get('instance_id', None)
        self.pool = attributes.get('pool', None)
