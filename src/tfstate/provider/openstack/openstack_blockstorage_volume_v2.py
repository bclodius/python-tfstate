# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.provider.openstack import OpenStackResource
from tfstate.exceptions import InvalidResource


class OSBlockstorageVolumeV2(OpenStackResource):
    """
    Provides an OpenStack V2 Blockstorage Volume.

    Usage::

        OSBlockstorageVolumeV2(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "openstack_blockstorage_volume_v2":
            raise InvalidResource(
                "OSBlockstorageVolumeV2 must be of 'openstack_blockstorage_volume_v2' type")
        attributes = self.primary_data['attributes']
        self.attachment = self.compound_attributes.get('attachment', {})
        self.availability_zone = attributes.get('availability_zone', None)
        self.description = attributes.get('description', None)
        self.metadata = self.compound_attributes.get('metadata', {})
        self.name = attributes.get('name', None)
        self.size = attributes.get('size', None)
        self.snapshot_id = attributes.get('snapshot_id', None)
        self.source_vol_id = attributes.get('source_vol_id', None)
        self.volume_type = attributes.get('volume_type', None)
