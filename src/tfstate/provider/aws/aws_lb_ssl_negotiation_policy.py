# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsLBSSLNegotiationPolicyResource(AwsResource):
    """
    Provides a resource to create an AWS VPC routing.

    Usage::

        AwsLBSSLNegotiationPolicyResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_lb_ssl_negotiation_policy":
            raise InvalidResource("AwsLBSSLNegotiationPolicyResource must be of 'aws_lb_ssl_negotiation_policy' type")
        attributes = self.primary_data['attributes']
        self.attribute = self.compound_attributes.get('attribute', {})
        self.id = attributes.get('id', None)
        self.lb_port = attributes.get('lb_port', None)
        self.load_balancer = attributes.get('load_balancer', None)
        self.name = attributes.get('name', None)
