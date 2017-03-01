# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.aws import AwsResource
from tfstate.exceptions import InvalidResource


class DataAwsAmiResource(AwsResource):
    """
    Provides a resource to create an AWS VPC routing.

    Usage::

        DataAwsAmiResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "aws_ami":
            raise InvalidResource("DataAwsAmiResource must be of 'aws_ami' type")
        attributes = self.primary_data['attributes']
        self.architecture = attributes.get('architecture', None)
        self.block_device_mappings = self.compound_attributes.get('block_device_mappings', {})
        self.creation_date = attributes.get('creation_date', None)
        self.description = attributes.get('description', None)
        self.hypervisor = attributes.get('hypervisor', None)
        self.id = attributes.get('id', None)
        self.image_id = attributes.get('image_id', None)
        self.image_location = attributes.get('image_location', None)
        self.image_type = attributes.get('image_type', None)
        self.most_recent = attributes.get('most_recent', None)
        self.name = attributes.get('name', None)
        self.public = attributes.get('public', None)
        self.root_device_name = attributes.get('root_device_name', None)
        self.root_device_type = attributes.get('root_device_type', None)
        self.sriov_net_support = attributes.get('sriov_net_support', None)
        self.state = attributes.get('state', None)
        self.tags = self.compound_attributes.get('tags', {})
        self.virtualization_type = attributes.get('virtualization_type', None)
