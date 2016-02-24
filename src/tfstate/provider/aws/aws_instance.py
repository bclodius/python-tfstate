# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class AwsInstanceResource(AwsResource):
    """
    Provides an AWS VPC subnet resource.

    Usage::

        AwsInstanceResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_instance":
            raise InvalidResource("AwsInstanceResource must be of 'aws_instance' type")
        attributes = self.primary_data['attributes']
        self.ami = attributes['ami']
        self.availability_zone = attributes['availability_zone']
        self.iam_instance_profile = attributes['iam_instance_profile']
        self.instance_type = attributes['instance_type']
        self.key_name = attributes['key_name']
        self.private_dns = attributes['private_dns']
        self.private_ip = attributes['private_ip']
        self.public_dns = attributes['public_dns']
        self.public_ip = attributes['public_ip']
        self.subnet_id = attributes['subnet_id']
        self.tenancy = attributes['tenancy']
        self.associate_public_ip_address = self.get_boolean_attribute('associate_public_ip_address')
        self.ebs_optimized = self.get_boolean_attribute('ebs_optimized')
        self.monitoring = self.get_boolean_attribute('monitoring')
        self.source_dest_check = self.get_boolean_attribute('source_dest_check')
        self.tags = self.compound_attributes.get('tags', {})
        self.ebs_block_device = self.compound_attributes.get('ebs_block_device', {})
        self.ephemeral_block_device = self.compound_attributes.get('ephemeral_block_device', {})
        self.root_block_device = self.compound_attributes.get('root_block_device', {})
        self.security_groups = self.compound_attributes.get('security_groups', {})
        self.vpc_security_group_ids = self.compound_attributes.get('vpc_security_group_ids', {})
