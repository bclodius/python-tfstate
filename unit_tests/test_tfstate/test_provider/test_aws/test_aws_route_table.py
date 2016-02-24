# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# Python tfstate
from tfstate.provider.aws import AwsResource, AwsRouteTableResource
from tfstate.exceptions import InvalidResource

# Unit tests
from unit_tests.base import BaseResourceUnitTest


class AwsRouteTableResourceUnitTest(BaseResourceUnitTest):
    def test_object_constructor(self):
        self.load_example_json('aws/aws_route_table/aws_route_table_example.json')
        resource_name, resource_data = self.example_data.popitem()
        rt_resource = AwsRouteTableResource(resource_name, resource_data)
        self.assertIsInstance(
            rt_resource, AwsResource, "AwsRouteTableResource object does not inherit from AwsResource")
        self.assertEqual(
            rt_resource.resource_type, "aws_route_table", "Resource type is not aws_route_table")
        # Attribute checks
        native_primary = rt_resource.primary_data
        native_attributes = native_primary['attributes']
        self.assertEqual(rt_resource.id, native_primary['id'], "Resource ID does not match")
        self.assertEqual(rt_resource.vpc_id, native_attributes['vpc_id'], "Resource vpc_id does not match")
        # Tags checking
        self.assertTrue(hasattr(rt_resource, 'tags'), "Resource tags does not exist")
        self.assertEqual(rt_resource.tags['Env'], native_attributes['tags.Env'], 'Tag Env does not match')
        self.assertEqual(rt_resource.tags['Name'], native_attributes['tags.Name'], 'Tag Name does not match')
        self.assertEqual(
            rt_resource.tags['Billing'], native_attributes['tags.Billing'], 'Tag Billing does not match')
        # Routes checking
        self.assertTrue(hasattr(rt_resource, 'routes'), "Resource routes does not exist")
        for route, route_data in rt_resource.routes.items():
            self.assertIn('network_interface_id', route_data, 'Network interface id missing from route data')
            self.assertIn('gateway_id', route_data, 'Gateway id missing from route data')
            self.assertIn('instance_id', route_data, 'Instance id missing from route data')
            self.assertIn(
                'vpc_peering_connection_id', route_data, 'VPC peering connection id missing from route data')
            self.assertIn('cidr_block', route_data, 'CIDR block missing from route data')

        self.assertTrue(hasattr(rt_resource, 'propagating_vgws'), "Resource propagating VGWs does not exist")

    def test_object_constructor_invalid_type(self):
        self.load_example_json('aws/aws_route_table/aws_route_table_example_invalid_type.json')
        resource_name, resource_data = self.example_data.popitem()
        with self.assertRaises(InvalidResource):
            AwsRouteTableResource(resource_name, resource_data)


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(AwsRouteTableResourceUnitTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
