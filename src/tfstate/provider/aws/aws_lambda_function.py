# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsLambdaFunctionResource(AwsResource):
    """
    Provides a resource to create an AWS VPC routing.

    Usage::

        AwsLambdaFunctionResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_lambda_function":
            raise InvalidResource("AwsLambdaFunctionResource must be of 'aws_lambda_function' type")
        attributes = self.primary_data['attributes']
        self.arn = attributes.get('arn', None)
        self.description = attributes.get('description', None)
        self.environment = self.compound_attributes.get('environment', {})
        self.filename = attributes.get('filename', None)
        self.function_name = attributes.get('function_name', None)
        self.handler = attributes.get('handler', None)
        self.id = attributes.get('id', None)
        self.kms_key_arn = attributes.get('kms_key_arn', None)
        self.last_modified = attributes.get('last_modified', None)
        self.memory_size = attributes.get('memory_size', None)
        self.publish = attributes.get('publish', None)
        self.qualified_arn = attributes.get('qualified_arn', None)
        self.role = attributes.get('role', None)
        self.runtime = attributes.get('runtime', None)
        self.source_code_hash = attributes.get('source_code_hash', None)
        self.timeout = attributes.get('timeout', None)
        self.version = attributes.get('version', None)
        self.vpc_config = self.compound_attributes.get('vpc_config', {})
