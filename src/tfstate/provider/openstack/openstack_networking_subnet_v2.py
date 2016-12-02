# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.openstack import OpenStackResource
from tfstate.exceptions import InvalidResource


class OSNetworkingSubnetV2(OpenStackResource):
    """
    Provides an OpenStack V2 Networking Subnet.

    Usage::

        OSNetworkingSubnetV2(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "openstack_networking_subnet_v2":
            raise InvalidResource(
                "OSNetworkingSubnetV2 must be of 'openstack_networking_subnet_v2' type")
        attributes = self.primary_data['attributes']
        self.cidr = attributes.get('cidr', None)
        self.dns_nameservers = self.compound_attributes.get('dns_nameservers', {})
        self.enable_dhcp = self.get_boolean_attribute('enable_dhcp')
        self.gateway_ip = attributes.get('gateway_ip', None)
        self.host_routes = self.compound_attributes.get('host_routes', {})
        self.ip_version = attributes.get('ip_version', None)
        self.name = attributes.get('name', None)
        self.network_id = attributes.get('network_id', None)
        self.tenant_id = attributes.get('tenant_id', None)
