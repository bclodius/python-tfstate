# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsEipResource(AwsResource):
    """
    Provides an AWS Elastic IP resource

    Usage::

        AwsEipResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_eip":
            raise InvalidResource("AwsEipResource must be of 'aws_eip' type")

        self.id = self.primary_data['id']
        attributes = self.primary_data['attributes']
        self.association_id = attributes['association_id']
        self.domain = attributes['domain']
        self.instance = attributes['instance']
        self.network_interface = attributes['network_interface']
        self.private_ip = attributes['private_ip']
        self.public_ip = attributes['public_ip']
        self.vpc = attributes['vpc']
