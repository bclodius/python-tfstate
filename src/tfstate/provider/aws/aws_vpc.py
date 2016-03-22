# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsVpcResource(AwsResource):
    """
    Provides an AWS VPC resource.

    Usage::

        AwsVpcResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_vpc":
            raise InvalidResource("AwsVpcResource must be of 'aws_vpc' type")
        attributes = self.primary_data['attributes']
        self.cidr_block = attributes.get('cidr_block', None)
        self.default_network_acl_id = attributes.get('default_network_acl_id', None)
        self.default_security_group_id = attributes.get('default_security_group_id', None)
        self.dhcp_options_id = attributes.get('dhcp_options_id', None)
        self.enable_dns_hostnames = self.get_boolean_attribute('enable_dns_hostnames')
        self.enable_dns_support = self.get_boolean_attribute('enable_dns_support')
        self.main_route_table_id = attributes.get('main_route_table_id', None)
        self.tags = self.compound_attributes.get('tags', {})
