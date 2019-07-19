# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# Python tfstate
from tfstate.exceptions import InvalidResource
from tfstate.base import Resource
from tfstate.provider.other.null_data_source import NullDataSource

# Unit tests
from unit_tests.base import BaseResourceUnitTest


class DataNullResourceUnitTest(BaseResourceUnitTest):
    def test_object_constructor(self):
        self.load_example_json('other/null_resource/data_null_resource_example.json')
        resource_name, resource_data = self.example_data.popitem()
        null_resource = NullDataSource(resource_name, resource_data)
        self.assertIsInstance(null_resource, Resource, "NullDataSource object does not inherit from AwsResource")
        self.assertEqual(null_resource.resource_type, "null_data_source", "Resource type is not null_data_source")
        # Attribute checks
        native_primary = null_resource.primary_data
        self.assertEqual(null_resource.id, native_primary['id'], "Resource ID does not match")


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(DataNullResourceUnitTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
