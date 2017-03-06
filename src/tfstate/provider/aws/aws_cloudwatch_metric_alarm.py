# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsCloudWatchMetricAlarmResource(AwsResource):
    """
    Provides a resource to create an AWS VPC routing.

    Usage::

        AwsCloudWatchMetricAlarmResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_cloudwatch_metric_alarm":
            raise InvalidResource("AwsCloudWatchMetricAlarmResource must be of 'aws_cloudwatch_metric_alarm' type")
        attributes = self.primary_data['attributes']
        self.actions_enabled = attributes.get('actions_enabled', None)
        self.alarm_actions = self.compound_attributes.get('alarm_actions', {})
        self.alarm_description = attributes.get('alarm_description', None)
        self.alarm_name = attributes.get('alarm_name', None)
        self.comparison_operator = attributes.get('comparison_operator', None)
        self.dimensions = self.compound_attributes.get('dimensions', {})
        self.evaluation_periods = attributes.get('evaluation_periods', None)
        self.id = attributes.get('id', None)
        self.insufficient_data_actions = self.compound_attributes.get('insufficient_data_actions', {})
        self.metric_name = attributes.get('metric_name', None)
        self.namespace = attributes.get('namespace', None)
        self.ok_actions = self.compound_attributes.get('ok_actions', {})
        self.period = attributes.get('period', None)
        self.statistic = attributes.get('statistic', None)
        self.threshold = attributes.get('threshold', None)
        self.unit = attributes.get('unit', None)
