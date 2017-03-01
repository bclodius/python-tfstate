# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsElasticCacheSubnetGroupResource(AwsResource):
    """
    Provides a resource to create an AWS VPC routing.

    Usage::

        AwsElasticCacheSubnetGroupResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_elasticache_subnet_group":
            raise InvalidResource("AwsElasticCacheSubnetGroupResource must be of 'aws_elasticache_subnet_group' type")
        attributes = self.primary_data['attributes']
        self.description = attributes.get('description', None)
        self.id = attributes.get('id', None)
        self.name = attributes.get('name', None)
        self.subnet_ids = self.compound_attributes.get('subnet_ids', {})
