# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# py.test
import pytest

# Python tfstate
from tfstate.provider.aws import AwsResource, AwsEipResource
from tfstate.exceptions import InvalidResource

# Unit tests
from unit_tests.base import BaseResourceUnitTest


@pytest.mark.provider_aws
class AwsEipResourceUnitTest(BaseResourceUnitTest):
    def test_object_constructor(self):
        self.load_example_json('aws/aws_eip/aws_eip_example.json')
        resource_name, resource_data = self.example_data.popitem()
        eip_resource = AwsEipResource(resource_name, resource_data)
        self.assertIsInstance(eip_resource, AwsResource, "AwsEipResource object does not inherit from AwsResource")
        self.assertEqual(eip_resource.resource_type, "aws_eip", "Resource type is not aws_eip")
        # Attribute checks
        native_primary = eip_resource.primary_data
        native_attributes = native_primary['attributes']
        self.assertEqual(eip_resource.id, native_primary['id'], "Resource ID does not match")
        self.assertEqual(eip_resource.id, native_attributes['id'], "Resource ID does not match")
        self.assertEqual(
            eip_resource.association_id, native_attributes['association_id'], "Resource association_id does not match")
        self.assertEqual(eip_resource.domain, native_attributes['domain'], "Resource domain does not match")
        self.assertEqual(eip_resource.instance, native_attributes['instance'], "Resource instance does not match")
        self.assertEqual(
            eip_resource.network_interface, native_attributes['network_interface'],
            "Resource network_interface does not match")
        self.assertEqual(
            eip_resource.private_ip, native_attributes['private_ip'], "Resource private_ip does not match")
        self.assertEqual(
            eip_resource.public_ip, native_attributes['public_ip'], "Resource public_ip does not match")
        self.assertEqual(eip_resource.vpc, native_attributes['vpc'], "Resource vpc does not match")

    def test_object_constructor_invalid_type(self):
        self.load_example_json('aws/aws_eip/aws_eip_example_invalid_type.json')
        resource_name, resource_data = self.example_data.popitem()
        with self.assertRaises(InvalidResource):
            AwsEipResource(resource_name, resource_data)


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(AwsEipResourceUnitTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
