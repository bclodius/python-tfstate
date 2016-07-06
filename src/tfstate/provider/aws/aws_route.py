# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsRouteResource(AwsResource):
    """
    Provides a resource to create an AWS VPC routing.

    Usage::

        AwsRouteResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_route":
            raise InvalidResource("AwsRouteResource must be of 'aws_route' type")
        attributes = self.primary_data['attributes']
        self.vpc_id = attributes.get('vpc_id', None)

        self.tags = self.compound_attributes.get('tags', {})
        self.routes = self.compound_attributes.get('route', {})
        self.propagating_vgws = self.compound_attributes.get('propagating_vgws', {})
