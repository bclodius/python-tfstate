# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsAutoScalingPolicyResource(AwsResource):
    """
    Provides a resource to create an AWS VPC routing.

    Usage::

        AwsAutoScalingPolicyResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_autoscaling_policy":
            raise InvalidResource("AwsAutoScalingPolicyResource must be of 'aws_autoscaling_policy' type")
        attributes = self.primary_data['attributes']
        self.adjustment_type = attributes.get('adjustment_type', None)
        self.arn = attributes.get('arn', None)
        self.autoscaling_group_name = attributes.get('autoscaling_group_name', None)
        self.cooldown = attributes.get('cooldown', None)
        self.estimated_instance_warmup = attributes.get('estimated_instance_warmup', None)
        self.id = attributes.get('id', None)
        self.metric_aggregation_type = attributes.get('metric_aggregation_type', None)
        self.min_adjustment_step = attributes.get('min_adjustment_step', None)
        self.name = attributes.get('name', None)
        self.policy_type = attributes.get('policy_type', None)
        self.scaling_adjustment = attributes.get('scaling_adjustment', None)
