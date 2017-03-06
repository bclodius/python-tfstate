# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class DataAwsCallerIdentityResource(AwsResource):
    """
    Provides a resource to create an AWS VPC routing.

    Usage::

        DataAwsCallerIdentityResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_caller_identity":
            raise InvalidResource("DataAwsCallerIdentityResource must be of 'aws_caller_identity' type")
        attributes = self.primary_data['attributes']
        self.account_id = attributes.get('account_id', None)
        self.id = attributes.get('id', None)
