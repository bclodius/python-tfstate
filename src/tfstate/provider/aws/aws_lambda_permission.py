# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsLambdaPermissionResource(AwsResource):
    """
    Provides a resource to create an AWS VPC routing.

    Usage::

        AwsLambdaPermissionResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_lambda_permission":
            raise InvalidResource("AwsLambdaPermissionResource must be of 'aws_lambda_permission' type")
        attributes = self.primary_data['attributes']
        self.action = attributes.get('action', None)
        self.function_name = attributes.get('function_name', None)
        self.id = attributes.get('id', None)
        self.principal = attributes.get('principal', None)
        self.source_arn = attributes.get('source_arn', None)
        self.statement_id = attributes.get('statement_id', None)
