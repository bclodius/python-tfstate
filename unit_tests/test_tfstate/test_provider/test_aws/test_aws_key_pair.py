# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# py.test
import pytest

# Python tfstate
from tfstate.provider.aws import AwsResource, AwsKeyPairResource
from tfstate.exceptions import InvalidResource

# Unit tests
from unit_tests.base import BaseResourceUnitTest


@pytest.mark.provider_aws
class AwsKeyPairResourceUnitTest(BaseResourceUnitTest):
    def test_object_constructor(self):
        self.load_example_json('aws/aws_key_pair/aws_key_pair_example.json')
        resource_name, resource_data = self.example_data.popitem()
        key_pair_resource = AwsKeyPairResource(resource_name, resource_data)
        self.assertIsInstance(
            key_pair_resource, AwsResource, "AwsKeyPairResource object does not inherit from AwsResource")
        self.assertEqual(key_pair_resource.resource_type, "aws_key_pair", "Resource type is not aws_key_pair")
        # Attribute checks
        native_primary = key_pair_resource.primary_data
        native_attributes = native_primary['attributes']
        native_meta = native_primary['meta']
        self.assertEqual(key_pair_resource.id, native_primary['id'], "Resource ID does not match")
        self.assertEqual(
            key_pair_resource.key_name, native_attributes['key_name'], "Resource key_name does not match")
        self.assertEqual(
            key_pair_resource.public_key, native_attributes['public_key'], "Resource public_key does not match")
        self.assertEqual(
            key_pair_resource.metadata, native_meta, "Resource metadata does not match")

    def test_object_constructor_invalid_type(self):
        self.load_example_json(
            'aws/aws_key_pair/aws_key_pair_example_invalid_type.json')
        resource_name, resource_data = self.example_data.popitem()
        with self.assertRaises(InvalidResource):
            AwsKeyPairResource(resource_name, resource_data)


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(AwsKeyPairResourceUnitTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
