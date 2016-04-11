# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsIamServerCertificateResource(AwsResource):
    """
    Provides an AWS IAM Server Certificate resource

    Usage::

        AwsIamServerCertificateResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_iam_server_certificate":
            raise InvalidResource("AwsIamServerCertificateResource must be of 'aws_iam_server_certificate' type")

        attributes = self.primary_data['attributes']
        self.arn = attributes.get('arn', None)
        self.certificate_body = attributes.get('certificate_body', None)
        self.name = attributes.get('name', None)
        self.path = attributes.get('path', None)
        self.private_key = attributes.get('private_key', None)
