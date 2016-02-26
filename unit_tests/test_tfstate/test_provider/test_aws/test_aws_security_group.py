# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# py.test
import pytest

# Python tfstate
from tfstate.provider.aws import AwsResource, AwsSecurityGroupResource
from tfstate.exceptions import InvalidResource

# Unit tests
from unit_tests.base import BaseResourceUnitTest


@pytest.mark.provider_aws
class AwsSecurityGroupResourceUnitTest(BaseResourceUnitTest):
    def test_object_constructor(self):
        self.load_example_json('aws/aws_security_group/aws_security_group_example.json')
        resource_name, resource_data = self.example_data.popitem()
        sg_resource = AwsSecurityGroupResource(resource_name, resource_data)
        self.assertIsInstance(
            sg_resource, AwsResource, "AwsSecurityGroupResource object does not inherit from AwsResource")
        self.assertEqual(
            sg_resource.resource_type, "aws_security_group", "Resource type is not aws_security_group")
        # Attribute checks
        native_primary = sg_resource.primary_data
        native_attributes = native_primary['attributes']
        self.assertEqual(sg_resource.id, native_primary['id'], "Resource ID does not match")
        self.assertEqual(
            sg_resource.description, native_attributes['description'], "Resource description does not match")
        self.assertEqual(sg_resource.name, native_attributes['name'], "Resource name does not match")
        self.assertEqual(sg_resource.owner_id, native_attributes['owner_id'], "Resource owner_id does not match")
        self.assertEqual(sg_resource.vpc_id, native_attributes['vpc_id'], "Resource vpc_id does not match")
        # Tags checking
        self.check_tags(sg_resource, native_attributes)
        # Egress rules
        self.assertTrue(hasattr(sg_resource, "egress"), "Resource egress does not exist")
        egress_count = int(native_attributes['egress.#'])
        self.assertEqual(len(sg_resource.egress), egress_count, 'Resource egress count does not match')
        # Ingress rules
        self.assertTrue(hasattr(sg_resource, "ingress"), "Resource ingress does not exist")
        ingress_count = int(native_attributes['ingress.#'])
        self.assertEqual(len(sg_resource.ingress), ingress_count, 'Resource ingress count does not match')

    def test_object_constructor_invalid_type(self):
        self.load_example_json(
            'aws/aws_security_group/aws_security_group_example_invalid_type.json')
        resource_name, resource_data = self.example_data.popitem()
        with self.assertRaises(InvalidResource):
            AwsSecurityGroupResource(resource_name, resource_data)


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(AwsSecurityGroupResourceUnitTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
