# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.openstack import OpenStackResource
from tfstate.exceptions import InvalidResource


class OSComputeKeypairV2(OpenStackResource):
    """
    Provides an OpenStack V2 Compute KeyPair

    Usage::

        OSComputeKeypairV2(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "openstack_compute_keypair_v2":
            raise InvalidResource(
                "OSComputeKeypairV2 must be of 'openstack_compute_keypair_v2' type")
        attributes = self.primary_data['attributes']
        self.name = attributes.get('name', None)
        self.public_key = attributes.get('public_key', None)
