# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsNatGatewayResource(AwsResource):
    """
    Provides an AWS NAT Gateway resource

    Usage::

        AwsNatGatewayResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_nat_gateway":
            raise InvalidResource("AwsNatGatewayResource must be of 'aws_nat_gateway' type")

        attributes = self.primary_data['attributes']
        self.allocation_id = attributes.get('allocation_id', None)
        self.network_interface_id = attributes.get('network_interface_id', None)
        self.private_ip = attributes.get('private_ip', None)
        self.public_ip = attributes.get('public_ip', None)
        self.subnet_id = attributes.get('subnet_id', None)
