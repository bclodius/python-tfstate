# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsProxyProtocolPolicyResource(AwsResource):
    """
    Provides a resource to create an AWS VPC routing.

    Usage::

        AwsProxyProtocolPolicyResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_proxy_protocol_policy":
            raise InvalidResource("AwsProxyProtocolPolicyResource must be of 'aws_proxy_protocol_policy' type")
        attributes = self.primary_data['attributes']
        self.id = attributes.get('id', None)
        self.instance_ports = self.compound_attributes.get('instance_ports', {})
        self.load_balancer = attributes.get('load_balancer', None)
