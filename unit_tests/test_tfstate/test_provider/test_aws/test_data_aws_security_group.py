# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# py.test
import pytest

# Python tfstate
from tfstate.provider.aws import AwsResource, DataAwsSecurityGroupResource

# Unit tests
from unit_tests.base import BaseResourceUnitTest


@pytest.mark.provider_aws
class DataAwsSecurityGroupResourceUnitTest(BaseResourceUnitTest):
    def test_object_constructor(self):
        self.load_example_json('aws/data_aws_security_group/data_aws_security_group_example.json')
        resource_name, resource_data = self.example_data.popitem()
        sg_resource = DataAwsSecurityGroupResource(resource_name, resource_data)
        self.assertIsInstance(
            sg_resource, AwsResource, "DataAwsSecurityGroupResource object does not inherit from AwsResource")
        self.assertEqual(
            sg_resource.resource_type, "aws_security_group", "Resource type is not aws_security_group")
        # Attribute checks
        native_primary = sg_resource.primary_data
        native_attributes = native_primary['attributes']
        self.assertEqual(sg_resource.id, native_primary['id'], "Resource ID does not match")
        self.assertEqual(sg_resource.arn, native_attributes['arn'], "Arn does not match")
        self.assertEqual(sg_resource.description, native_attributes['description'], "Description does not match")
        self.assertEqual(sg_resource.name, native_attributes['name'], "Resource name does not match")
        self.assertEqual(sg_resource.vpc_id, native_attributes['vpc_id'], "VpcId does not match")
        self.check_tags(sg_resource, native_attributes)



def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(DataAwsSecurityGroupResourceUnitTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
