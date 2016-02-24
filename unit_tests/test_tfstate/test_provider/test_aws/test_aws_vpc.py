# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# Python tfstate
from tfstate.provider.aws import AwsResource, AwsVpcResource
from tfstate.exceptions import InvalidResource

# Unit tests
from unit_tests.base import BaseResourceUnitTest


class AwsVpcResourceUnitTest(BaseResourceUnitTest):
    def test_object_constructor(self):
        self.load_example_json('aws/aws_vpc/aws_vpc_example.json')
        resource_name, resource_data = self.example_data.popitem()
        vpc_resource = AwsVpcResource(resource_name, resource_data)
        self.assertIsInstance(
            vpc_resource, AwsResource, "AwsVpcResource object does not inherit from AwsResource")
        self.assertEqual(vpc_resource.resource_type, "aws_vpc", "Resource type is not aws_vpc")
        # Attribute checks
        native_primary = vpc_resource.primary_data
        native_attributes = native_primary['attributes']
        self.assertEqual(vpc_resource.id, native_primary['id'], "Resource ID does not match")
        self.assertEqual(
            vpc_resource.cidr_block, native_attributes['cidr_block'], "Resource CIDR block does not match")
        self.assertEqual(
            vpc_resource.default_network_acl_id, native_attributes['default_network_acl_id'],
            "Resource default_network_acl_id does not match")
        self.assertEqual(
            vpc_resource.default_security_group_id, native_attributes['default_security_group_id'],
            "Resource default_security_group_id does not match")
        self.assertEqual(
            vpc_resource.dhcp_options_id, native_attributes['dhcp_options_id'],
            "Resource dhcp_options_id does not match")
        enable_dns_hostnames = True if native_attributes['enable_dns_hostnames'] == 'true' else False
        self.assertEqual(
            vpc_resource.enable_dns_hostnames, enable_dns_hostnames, "Resource enable_dns_hostnames does not match")
        enable_dns_support = True if native_attributes['enable_dns_support'] == 'true' else False
        self.assertEqual(
            vpc_resource.enable_dns_support, enable_dns_support, "Resource enable_dns_support does not match")
        self.assertEqual(
            vpc_resource.main_route_table_id, native_attributes['main_route_table_id'],
            "Resource main_route_table_id does not match")
        # Tags checking
        self.check_tags(vpc_resource, native_attributes)

    def test_object_constructor_invalid_type(self):
        self.load_example_json(
            'aws/aws_vpc/aws_vpc_example_invalid_type.json')
        resource_name, resource_data = self.example_data.popitem()
        with self.assertRaises(InvalidResource):
            AwsVpcResource(resource_name, resource_data)


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(AwsVpcResourceUnitTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
