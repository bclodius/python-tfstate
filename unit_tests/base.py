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
    def setUp(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        example_file = open(os.path.join(base_path, '../tfstate_examples', self.example_json), 'r')
        self.example_data = json.load(example_file)
