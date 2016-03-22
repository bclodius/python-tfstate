# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsSecurityGroupResource(AwsResource):
    """
    Provides an AWS security group resource.

    Usage::

        AwsSecurityGroupResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_security_group":
            raise InvalidResource("AwsSecurityGroupResource must be of 'aws_security_group' type")
        attributes = self.primary_data['attributes']
        self.description = attributes.get('description', None)
        self.name = attributes.get('name', None)
        self.owner_id = attributes.get('owner_id', None)
        self.vpc_id = attributes.get('vpc_id', None)
        self.tags = self.compound_attributes.get('tags', {})
        self.egress = self.compound_attributes.get('egress', {})
        self.ingress = self.compound_attributes.get('ingress', {})
