# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsSnsTopicSubscriptionResource(AwsResource):
    """
    Provides a resource to create an AWS VPC routing.

    Usage::

        AwsSnsTopicSubscriptionResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_sns_topic_subscription":
            raise InvalidResource("AwsSnsTopicSubscriptionResource must be of 'aws_sns_topic_subscription' type")
        attributes = self.primary_data['attributes']
        self.arn = attributes.get('arn', None)
        self.confirmation_timeout_in_minutes = attributes.get('confirmation_timeout_in_minutes', None)
        self.endpoint = attributes.get('endpoint', None)
        self.endpoint_auto_confirms = attributes.get('endpoint_auto_confirms', None)
        self.id = attributes.get('id', None)
        self.protocol = attributes.get('protocol', None)
        self.raw_message_delivery = attributes.get('raw_message_delivery', None)
        self.topic_arn = attributes.get('topic_arn', None)
