# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsAutoScalingGroupResource(AwsResource):
    """
    Provides a resource to create an AWS VPC routing.

    Usage::

        AwsAutoScalingGroupResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_autoscaling_group":
            raise InvalidResource("AwsAutoScalingGroupResource must be of 'aws_autoscaling_group' type")
        attributes = self.primary_data['attributes']
        self.arn = attributes.get('arn', None)
        self.availability_zones = self.compound_attributes.get('availability_zones', {})
        self.default_cooldown = attributes.get('default_cooldown', None)
        self.desired_capacity = attributes.get('desired_capacity', None)
        self.force_delete = attributes.get('force_delete', None)
        self.health_check_grace_period = attributes.get('health_check_grace_period', None)
        self.health_check_type = attributes.get('health_check_type', None)
        self.id = attributes.get('id', None)
        self.launch_configuration = attributes.get('launch_configuration', None)
        self.load_balancers = self.compound_attributes.get('load_balancers', {})
        self.max_size = attributes.get('max_size', None)
        self.metrics_granularity = attributes.get('metrics_granularity', None)
        self.min_size = attributes.get('min_size', None)
        self.name = attributes.get('name', None)
        self.placement_group = attributes.get('placement_group', None)
        self.protect_from_scale_in = attributes.get('protect_from_scale_in', None)
        self.tags = self.compound_attributes.get('tags', {})
        self.vpc_zone_identifier = self.compound_attributes.get('vpc_zone_identifier', {})
        self.wait_for_capacity_timeout = attributes.get('wait_for_capacity_timeout', None)
        self.wait_for_elb_capacity = attributes.get('wait_for_elb_capacity', None)
