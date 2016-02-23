# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsInternetGatewayResource(AwsResource):
    """
    Provides a resource to create a AWS VPC Internet Gateway

    Usage::

        AwsInternetGatewayResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_internet_gateway":
            raise InvalidResource("AwsInternetGatewayResource must be of 'aws_internet_gateway' type")
        attributes = self.primary_data['attributes']
        self.vpc_id = attributes['vpc_id']

        self.tags = self.compound_attributes.get('tags', {})
