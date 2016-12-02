# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.openstack import OpenStackResource
from tfstate.exceptions import InvalidResource


class OSComputeInstanceV2(OpenStackResource):
    """
    Provides an OpenStack V2 Networking Subnet.

    Usage::

        OSComputeInstanceV2(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "openstack_compute_instance_v2":
            raise InvalidResource(
                "OSComputeInstanceV2 must be of 'openstack_compute_instance_v2' type")
        attributes = self.primary_data['attributes']
        self.access_ip_v4 = attributes.get('access_ip_v4', None)
        self.access_ip_v6 = attributes.get('access_ip_v6', None)
        self.availability_zone = attributes.get('availability_zone', None)
        self.flavor_id = attributes.get('flavor_id', None)
        self.flavor_name = attributes.get('flavor_name', None)
        self.floating_ip = attributes.get('floating_ip', None)
        self.image_id = attributes.get('image_id', None)
        self.image_name = attributes.get('image_name', None)
        self.key_pair = attributes.get('key_pair', None)
        self.metadata = self.compound_attributes.get('metadata', {})
        self.name = attributes.get('name', None)
        self.network = self.compound_attributes.get('network', {})
        self.security_groups = self.compound_attributes.get('security_groups', {})
        self.stop_before_destroy = self.get_boolean_attribute('stop_before_destroy')
        self.user_data = attributes.get('user_data', None)
        self.volume = self.compound_attributes.get('volume', {})
