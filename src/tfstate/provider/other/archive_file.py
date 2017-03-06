# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.base import Resource
from tfstate.exceptions import InvalidResource


class ArchiveFileResource(Resource):
    """
    The null_resource is a resource that allows you to configure provisioners
    that are not directly associated with a single existing resource.

    Usage::

        ArchiveFileResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "archive_file":
            raise InvalidResource("ArchiveFileResource must be of 'archive_file' type")
        attributes = self.primary_data['attributes']
        self.id = attributes.get('id', None)
        self.output_base64sha256 = attributes.get('output_base64sha256', None)
        self.output_path = attributes.get('output_path', None)
        self.output_sha = attributes.get('output_sha', None)
        self.output_size = attributes.get('output_size', None)
        self.source_content = attributes.get('source_content', None)
        self.source_content_filename = attributes.get('source_content_filename', None)
        self.type = attributes.get('type', None)
