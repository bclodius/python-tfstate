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

        attributes = self.primary_data['attributes']
        self.association_id = attributes.get('association_id', None)
        self.domain = attributes.get('domain', None)
        self.instance = attributes.get('instance', None)
        self.network_interface = attributes.get('network_interface', None)
        self.private_ip = attributes.get('private_ip', None)
        self.public_ip = attributes.get('public_ip', None)
        self.vpc = attributes.get('vpc', None)
