# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# py.test
import pytest

# Python tfstate
from tfstate.provider.aws import AwsResource, AwsRouteTableAssociationResource
from tfstate.exceptions import InvalidResource

# Unit tests
from unit_tests.base import BaseResourceUnitTest


@pytest.mark.provider_aws
class AwsRouteTableAssociationResourceUnitTest(BaseResourceUnitTest):
    def test_object_constructor(self):
        self.load_example_json('aws/aws_route_table_association/aws_route_table_association_example.json')
        resource_name, resource_data = self.example_data.popitem()
        rta_resource = AwsRouteTableAssociationResource(resource_name, resource_data)
        self.assertIsInstance(
            rta_resource, AwsResource, "AwsRouteTableAssociationResource object does not inherit from AwsResource")
        self.assertEqual(
            rta_resource.resource_type, "aws_route_table_association",
            "Resource type is not aws_route_table_association")
        # Attribute checks
        native_primary = rta_resource.primary_data
        native_attributes = native_primary['attributes']
        self.assertEqual(rta_resource.id, native_primary['id'], "Resource ID does not match")
        self.assertEqual(
            rta_resource.route_table_id, native_attributes['route_table_id'],
            "Resource route_table_id does not match")
        self.assertEqual(rta_resource.subnet_id, native_attributes['subnet_id'], "Resource subnet_id does not match")

    def test_object_constructor_invalid_type(self):
        self.load_example_json(
            'aws/aws_route_table_association/aws_route_table_association_example_invalid_type.json')
        resource_name, resource_data = self.example_data.popitem()
        with self.assertRaises(InvalidResource):
            AwsRouteTableAssociationResource(resource_name, resource_data)


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(AwsRouteTableAssociationResourceUnitTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
