# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.openstack import OpenStackResource
from tfstate.exceptions import InvalidResource


class OSNetworkingSecgroupRuleV2(OpenStackResource):
    """
    Provides an OpenStack V2 Networking Security Group Rule.

    Usage::

        OSNetworkingSecgroupRuleV2(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "openstack_networking_secgroup_rule_v2":
            raise InvalidResource(
                "OSNetworkingSecgroupRuleV2 must be of 'openstack_networking_secgroup_rule_v2' type")
        attributes = self.primary_data['attributes']
        self.direction = attributes.get('direction', None)
        self.ethertype = attributes.get('ethertype', None)
        self.port_range_max = attributes.get('port_range_max', None)
        self.port_range_min = attributes.get('port_range_min', None)
        self.protocol = attributes.get('protocol', None)
        self.remote_group_id = attributes.get('remote_group_id', None)
        self.remote_ip_prefix = attributes.get('remote_ip_prefix', None)
        self.security_group_id = attributes.get('security_group_id', None)
        self.tenant_id = attributes.get('tenant_id', None)
