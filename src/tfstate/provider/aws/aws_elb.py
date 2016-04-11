# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsElbResource(AwsResource):
    """
    Provides an AWS ELB resource.

    Usage::

        AwsElbResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_elb":
            raise InvalidResource("AwsElbResource must be of 'aws_elb' type")
        attributes = self.primary_data['attributes']
        self.connection_draining = self.get_boolean_attribute('connection_draining')
        self.connection_draining_timeout = attributes.get('connection_draining_timeout', None)
        self.cross_zone_load_balancing = self.get_boolean_attribute('cross_zone_load_balancing')
        self.dns_name = attributes.get('dns_name', None)
        self.health_check = self.compound_attributes.get('health_check', {})
        self.idle_timeout = attributes.get('idle_timeout', None)
        self.instances = self.compound_attributes.get('instances', {})
        self.internal = self.get_boolean_attribute('internal')
        self.listener = self.compound_attributes.get('listener', {})
        self.name = attributes.get('name', None)
        self.security_groups = self.compound_attributes.get('security_groups', {})
        self.source_security_group = attributes.get('source_security_group', None)
        self.subnets = self.compound_attributes.get('subnets', {})
        self.tags = self.compound_attributes.get('tags', {})
        self.zone_id = attributes.get('zone_id', None)
