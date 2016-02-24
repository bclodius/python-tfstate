# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsSubnetResource(AwsResource):
    """
    Provides an AWS VPC subnet resource.

    Usage::

        AwsSubnetResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_subnet":
            raise InvalidResource("AwsSubnetResource must be of 'aws_subnet' type")
        attributes = self.primary_data['attributes']
        self.availability_zone = attributes['availability_zone']
        self.cidr_block = attributes['cidr_block']
        self.vpc_id = attributes['vpc_id']
        self.map_public_ip_on_launch = True if attributes['map_public_ip_on_launch'] == 'true' else False
        self.tags = self.compound_attributes.get('tags', {})
