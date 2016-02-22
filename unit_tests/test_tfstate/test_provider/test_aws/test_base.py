# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# Python tfstate
from tfstate.base import Resource
from tfstate.provider.aws import AwsResource

# Unit tests
from unit_tests.base import BaseResourceUnitTest


class AwsResourceUnitTest(BaseResourceUnitTest):
    example_json = 'aws_eip_example.json'

    def test_object_constructor(self):
        resource_name, resource_data = self.example_data.popitem()
        aws_resource = AwsResource(resource_name, resource_data)
        self.assertIsInstance(aws_resource, Resource, "AwsResource object does not inherit from Resource")
        self.assertEqual(aws_resource.provider, "aws", "AwsResource provider is not aws")
        self.assertEqual(aws_resource.name, resource_name, "AwsResource name does not match")
        self.assertEqual(aws_resource.native_data, resource_data, "AwsResource native data does not match")


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(AwsResourceUnitTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
