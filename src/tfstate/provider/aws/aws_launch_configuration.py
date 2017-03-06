# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsLaunchConfigurationResource(AwsResource):
    """
    Provides a resource to create an AWS VPC routing.

    Usage::

        AwsLaunchConfigurationResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_launch_configuration":
            raise InvalidResource("AwsLaunchConfigurationResource must be of 'aws_launch_configuration' type")
        attributes = self.primary_data['attributes']
        self.associate_public_ip_address = attributes.get('associate_public_ip_address', None)
        self.ebs_block_device = self.compound_attributes.get('ebs_block_device', {})
        self.ebs_optimized = attributes.get('ebs_optimized', None)
        self.enable_monitoring = attributes.get('enable_monitoring', None)
        self.ephemeral_block_device = self.compound_attributes.get('ephemeral_block_device', {})
        self.iam_instance_profile = attributes.get('iam_instance_profile', None)
        self.id = attributes.get('id', None)
        self.image_id = attributes.get('image_id', None)
        self.instance_type = attributes.get('instance_type', None)
        self.key_name = attributes.get('key_name', None)
        self.name = attributes.get('name', None)
        self.name_prefix = attributes.get('name_prefix', None)
        self.root_block_device = self.compound_attributes.get('root_block_device', {})
        self.security_groups = self.compound_attributes.get('security_groups', {})
        self.spot_price = attributes.get('spot_price', None)
        self.user_data = attributes.get('user_data', None)
        self.vpc_classic_link_id = attributes.get('vpc_classic_link_id', None)
        self.vpc_classic_link_security_groups = self.compound_attributes.get('vpc_classic_link_security_groups', {})
