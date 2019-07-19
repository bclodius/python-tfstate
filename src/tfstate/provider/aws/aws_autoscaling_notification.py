# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsAutoscalingNotificationResource(AwsResource):
    """
    Provides a resource to create an Autoscaling Notification.

    Usage::

        AwsAutoscalingNotificationResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_autoscaling_notification":
            raise InvalidResource("AwsAutoscalingNotificationResource must be of 'aws_autoscaling_notification' type")
        attributes = self.primary_data['attributes']
        self.id = attributes.get('id', None)
        self.topic_arn = attributes.get('topic_arn', None)
        self.notifications = self.compound_attributes.get('notifications', {})
        self.group_names = self.compound_attributes.get('group_names', {})