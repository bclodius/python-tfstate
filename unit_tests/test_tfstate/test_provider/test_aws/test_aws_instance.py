# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# py.test
import pytest

# Python tfstate
from tfstate.provider.aws import AwsResource, AwsInstanceResource
from tfstate.exceptions import InvalidResource

# Unit tests
from unit_tests.base import BaseResourceUnitTest


@pytest.mark.provider_aws
class AwsInstanceResourceUnitTest(BaseResourceUnitTest):
    def test_object_constructor(self):
        self.load_example_json('aws/aws_instance/aws_instance_example.json')
        resource_name, resource_data = self.example_data.popitem()
        ins_resource = AwsInstanceResource(resource_name, resource_data)
        self.assertIsInstance(
            ins_resource, AwsResource, "AwsInstanceResource object does not inherit from AwsResource")
        self.assertEqual(ins_resource.resource_type, "aws_instance", "Resource type is not aws_instance")
        # Attribute checks
        native_primary = ins_resource.primary_data
        native_attributes = native_primary['attributes']
        native_meta = native_primary['meta']
        self.assertEqual(ins_resource.id, native_primary['id'], "Resource ID does not match")
        self.assertEqual(ins_resource.ami, native_attributes['ami'], "Resource AMI does not match")
        self.assertEqual(
            ins_resource.availability_zone, native_attributes['availability_zone'],
            "Resource availability_zone does not match")
        self.assertEqual(
            ins_resource.iam_instance_profile, native_attributes['iam_instance_profile'],
            "Resource IAM instance profile does not match")
        self.assertEqual(
            ins_resource.instance_type, native_attributes['instance_type'], "Resource instance_type does not match")
        self.assertEqual(ins_resource.key_name, native_attributes['key_name'], "Resource key_name does not match")
        self.assertEqual(
            ins_resource.private_dns, native_attributes['private_dns'], "Resource private_dns does not match")
        self.assertEqual(
            ins_resource.private_ip, native_attributes['private_ip'], "Resource private_ip does not match")
        self.assertEqual(
            ins_resource.public_dns, native_attributes['public_dns'], "Resource public_dns does not match")
        self.assertEqual(
            ins_resource.public_ip, native_attributes['public_ip'], "Resource public_ip does not match")
        self.assertEqual(
            ins_resource.subnet_id, native_attributes['subnet_id'], "Resource subnet_id does not match")
        self.assertEqual(
            ins_resource.tenancy, native_attributes['tenancy'], "Resource tenancy does not match")
        associate_public_ip_address = True if native_attributes['associate_public_ip_address'] == 'true' else False
        ebs_optimized = True if native_attributes['ebs_optimized'] == 'true' else False
        monitoring = True if native_attributes['monitoring'] == 'true' else False
        source_dest_check = True if native_attributes['source_dest_check'] == 'true' else False
        self.assertEqual(
            ins_resource.associate_public_ip_address, associate_public_ip_address,
            "Resource associate_public_ip_address does not match")
        self.assertEqual(ins_resource.ebs_optimized, ebs_optimized, "Resource ebs_optimized does not match")
        self.assertEqual(ins_resource.monitoring, monitoring, "Resource monitoring does not match")
        self.assertEqual(
            ins_resource.source_dest_check, source_dest_check, "Resource source_dest_check does not match")
        # Tags checking
        self.check_tags(ins_resource, native_attributes)
        self.assertTrue(hasattr(ins_resource, 'ebs_block_device'), "Resource ebs_block_device does not exist")
        self.assertTrue(
            hasattr(ins_resource, 'ephemeral_block_device'), "Resource ephemeral_block_device does not exist")
        self.assertTrue(hasattr(ins_resource, 'root_block_device'), "Resource root_block_device does not exist")
        self.assertTrue(hasattr(ins_resource, 'security_groups'), "Resource security_groups does not exist")
        self.assertTrue(
            hasattr(ins_resource, 'vpc_security_group_ids'), "Resource vpc_security_group_ids does not exist")
        self.assertEqual(
            ins_resource.metadata, native_meta, "Resource metadata does not match")

    def test_object_constructor_invalid_type(self):
        self.load_example_json(
            'aws/aws_instance/aws_instance_example_invalid_type.json')
        resource_name, resource_data = self.example_data.popitem()
        with self.assertRaises(InvalidResource):
            AwsInstanceResource(resource_name, resource_data)


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(AwsInstanceResourceUnitTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
