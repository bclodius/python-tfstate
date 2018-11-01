# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class DataAwsSecurityGroupResource(AwsResource):
    """
    Provides a resource for data pulled security group.

    Usage::

        DataAwsSecurityGroupResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_security_group":
            raise InvalidResource("DataAwsSecurityGroupResource must be of 'aws_security_group' type")
        attributes = self.primary_data['attributes']
        self.arn = attributes.get('arn', None)
        self.description = attributes.get('description', None)
        self.id = attributes.get('id', None)
        self.name = attributes.get('name', None)
        self.tags = self.compound_attributes.get('tags', {})
        self.vpc_id = attributes.get('vpc_id', {})
