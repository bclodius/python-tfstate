# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# py.test
import pytest

# Python tfstate
from tfstate.provider.aws import AwsResource, AwsInternetGatewayResource
from tfstate.exceptions import InvalidResource

# Unit tests
from unit_tests.base import BaseResourceUnitTest


@pytest.mark.provider_aws
class AwsInternetGatewayResourceUnitTest(BaseResourceUnitTest):
    def test_object_constructor(self):
        self.load_example_json('aws/aws_internet_gateway/aws_internet_gateway_example.json')
        resource_name, resource_data = self.example_data.popitem()
        igw_resource = AwsInternetGatewayResource(resource_name, resource_data)
        self.assertIsInstance(
            igw_resource, AwsResource, "AwsInternetGatewayResource object does not inherit from AwsResource")
        self.assertEqual(
            igw_resource.resource_type, "aws_internet_gateway", "Resource type is not aws_internet_gateway")
        # Attribute checks
        native_primary = igw_resource.primary_data
        native_attributes = native_primary['attributes']
        self.assertEqual(igw_resource.id, native_primary['id'], "Resource ID does not match")
        self.assertEqual(igw_resource.vpc_id, native_attributes['vpc_id'], "Resource vpc_id does not match")
        # Tags checking
        self.check_tags(igw_resource, native_attributes)

    def test_object_constructor_invalid_type(self):
        self.load_example_json('aws/aws_internet_gateway/aws_internet_gateway_example_invalid_type.json')
        resource_name, resource_data = self.example_data.popitem()
        with self.assertRaises(InvalidResource):
            AwsInternetGatewayResource(resource_name, resource_data)


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(AwsInternetGatewayResourceUnitTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
