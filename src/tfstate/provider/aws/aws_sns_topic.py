# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsSnsTopicResource(AwsResource):
    """
    Provides a resource to create an AWS VPC routing.

    Usage::

        AwsSnsTopicResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_sns_topic":
            raise InvalidResource("AwsSnsTopicResource must be of 'aws_sns_topic' type")
        attributes = self.primary_data['attributes']
        self.arn = attributes.get('arn', None)
        self.display_name = attributes.get('display_name', None)
        self.id = attributes.get('id', None)
        self.name = attributes.get('name', None)
        self.policy = attributes.get('policy', None)
