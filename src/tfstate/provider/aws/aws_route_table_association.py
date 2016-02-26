# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsRouteTableAssociationResource(AwsResource):
    """
    Provides a resource to create an AWS VPC routing table.

    Usage::

        AwsRouteTableAssociationResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_route_table_association":
            raise InvalidResource("AwsRouteTableAssociationResource must be of 'aws_route_table_association' type")
        attributes = self.primary_data['attributes']
        self.route_table_id = attributes['route_table_id']
        self.subnet_id = attributes['subnet_id']
