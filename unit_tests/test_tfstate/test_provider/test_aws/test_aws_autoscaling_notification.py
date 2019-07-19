# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# py.test
import pytest

# Python tfstate
from tfstate.provider.aws import AwsResource, AwsAutoscalingNotificationResource

# Unit tests
from unit_tests.base import BaseResourceUnitTest


@pytest.mark.provider_aws
class AwsAutoscalingNotificationResourceUnitTest(BaseResourceUnitTest):
    def test_object_constructor(self):
        self.load_example_json('aws/aws_autoscaling_notification/aws_autoscaling_notification_example.json')
        resource_name, resource_data = self.example_data.popitem()
        notification_resource = AwsAutoscalingNotificationResource(resource_name, resource_data)
        self.assertIsInstance(
            notification_resource, AwsResource,
            "AwsAutoscalingNotificationResource object does not inherit from AwsResource")
        self.assertEqual(
            notification_resource.resource_type, "aws_autoscaling_notification",
            "Resource type is not aws_autoscaling_notification")
        # Attribute checks
        native_primary = notification_resource.primary_data
        native_attributes = native_primary['attributes']
        self.assertEqual(notification_resource.id, native_primary['id'], "Resource ID does not match")
        self.assertEqual(notification_resource.topic_arn, native_attributes['topic_arn'], "Topic arn does not match")
        self.assertTrue(hasattr(notification_resource, 'group_names'),
                        "group_names not found for aws_autoscaling_notification")
        self.assertTrue(hasattr(notification_resource, 'notifications'),
                        "notifications not found for aws_autoscaling_notification")


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(AwsAutoscalingNotificationResourceUnitTest))
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
