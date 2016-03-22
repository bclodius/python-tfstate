# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsKeyPairResource(AwsResource):
    """
    Provides an AWS EC2 key pair resource. A key pair is used to control login access to AWS EC2 instances.

    Usage::

        AwsKeyPairResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_key_pair":
            raise InvalidResource("AwsKeyPairResource must be of 'aws_key_pair' type")
        attributes = self.primary_data['attributes']
        self.key_name = attributes.get('key_name', None)
        self.public_key = attributes.get('public_key', None)
        self.metadata = self.primary_data['meta']
