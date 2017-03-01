# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsRoute53RecordResource(AwsResource):
    """
    Provides a resource to create an AWS VPC routing.

    Usage::

        AwsRouteResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_route53_record":
            raise InvalidResource("AwsRoute53RecordResource must be of 'aws_route53_record' type")
        attributes = self.primary_data['attributes']
        self.fqdn = attributes.get('fqdn', None)
        self.health_check_id = attributes.get('health_check_id', None)
        self.id = attributes.get('id', None)
        self.name = attributes.get('name', None)
        self.set_identifier = attributes.get('set_identifier', None)
        self.ttl = attributes.get('ttl', None)
        self.type = attributes.get('type', None)
        self.zone_id = attributes.get('zone_id', None)
