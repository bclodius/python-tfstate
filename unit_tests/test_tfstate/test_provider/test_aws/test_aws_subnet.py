# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# Python tfstate
from tfstate.provider.aws import AwsResource, AwsSubnetResource
from tfstate.exceptions import InvalidResource

# Unit tests
from unit_tests.base import BaseResourceUnitTest


class AwsSubnetResourceUnitTest(BaseResourceUnitTest):
    def test_object_constructor(self):
        self.load_example_json('aws/aws_subnet/aws_subnet_example.json')
        resource_name, resource_data = self.example_data.popitem()
        subnet_resource = AwsSubnetResource(resource_name, resource_data)
        self.assertIsInstance(
            subnet_resource, AwsResource, "AwsSubnetResource object does not inherit from AwsResource")
        self.assertEqual(subnet_resource.resource_type, "aws_subnet", "Resource type is not aws_subnet")
        # Attribute checks
        native_primary = subnet_resource.primary_data
        native_attributes = native_primary['attributes']
        self.assertEqual(subnet_resource.id, native_primary['id'], "Resource ID does not match")
        self.assertEqual(
            subnet_resource.availability_zone, native_attributes['availability_zone'],
            "Resource availability_zone does not match")
        self.assertEqual(
            subnet_resource.cidr_block, native_attributes['cidr_block'], "Resource CIDR block does not match")
        map_public_ip_on_launch = True if native_attributes['map_public_ip_on_launch'] == 'true' else False
        self.assertEqual(
            subnet_resource.map_public_ip_on_launch, map_public_ip_on_launch,
            "Resource map_public_ip_on_launch does not match")
        self.assertEqual(subnet_resource.vpc_id, native_attributes['vpc_id'], "Resource vpc_id does not match")
        self.check_tags(subnet_resource, native_attributes)

    def test_object_constructor_invalid_type(self):
        self.load_example_json(
            'aws/aws_subnet/aws_subnet_example_invalid_type.json')
        resource_name, resource_data = self.example_data.popitem()
        with self.assertRaises(InvalidResource):
            AwsSubnetResource(resource_name, resource_data)


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(AwsSubnetResourceUnitTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
