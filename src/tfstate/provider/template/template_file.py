# -*- coding: utf-8 -*-

# Python tfstate
from tfstate.base import Resource
from tfstate.exceptions import InvalidResource


class DataTemplateFileResource(Resource):
    """
    Provides a Data Template File

    Usage::

        DataTemplateFileResource(name, native_data)
    """

    def __init__(self, resource_name, native_data):
        super().__init__(resource_name, native_data)
        if self.resource_type != "template_file":
            raise InvalidResource("DataTemplateFileResource must be of 'template_file' type")
        attributes = self.primary_data['attributes']
        self.template = attributes.get('template', None)
        self.rendered = attributes.get('rendered', None)
        self.vars = self.compound_attributes.get('vars', {})
