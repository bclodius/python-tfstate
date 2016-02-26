# -*- coding: utf-8 -*-

# Python stdlib
import unittest
import os
import json


class BaseUnitTest(unittest.TestCase):
    def setUp(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.tfstate_path = os.path.join(base_path, '../tfstate_examples/first_example.tfstate')


class BaseResourceUnitTest(unittest.TestCase):
    def load_example_json(self, example_path):
        base_path = os.path.dirname(os.path.abspath(__file__))
        example_file = open(os.path.join(base_path, '../tfstate_examples', example_path), 'r')
        self.example_data = json.load(example_file)

    def check_tags(self, resource, native_attributes):
        # Tags checking
        self.assertTrue(hasattr(resource, 'tags'), "Resource tags does not exist")
        self.assertEqual(resource.tags['Env'], native_attributes['tags.Env'], 'Tag Env does not match')
        self.assertEqual(resource.tags['Name'], native_attributes['tags.Name'], 'Tag Name does not match')
        self.assertEqual(
            resource.tags['Billing'], native_attributes['tags.Billing'], 'Tag Billing does not match')
