# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# Python tfstate
from tfstate.exceptions import InvalidResource
from tfstate.base import Resource
from tfstate.null_resource import NullResource

# Unit tests
from unit_tests.base import BaseResourceUnitTest


class NullResourceUnitTest(BaseResourceUnitTest):
    def test_object_constructor(self):
        self.load_example_json('other/null_resource/null_resource_example.json')
        resource_name, resource_data = self.example_data.popitem()
        null_resource = NullResource(resource_name, resource_data)
        self.assertIsInstance(null_resource, Resource, "NullResource object does not inherit from AwsResource")
        self.assertEqual(null_resource.resource_type, "null_resource", "Resource type is not null_resource")
        # Attribute checks
        native_primary = null_resource.primary_data
        self.assertEqual(null_resource.id, native_primary['id'], "Resource ID does not match")

    def test_object_constructor_invalid_type(self):
        self.load_example_json('other/null_resource/null_resource_example_invalid_type.json')
        resource_name, resource_data = self.example_data.popitem()
        with self.assertRaises(InvalidResource):
            NullResource(resource_name, resource_data)


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(NullResourceUnitTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
