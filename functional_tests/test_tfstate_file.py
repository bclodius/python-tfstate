# -*- coding: utf-8 -*-

# Python stdlib
import unittest
import json

# Python tfstate
from tfstate import Tfstate

# Functional tests
from functional_tests.base import BaseFunctionalTest


class TfstateFileFunctionalTest(BaseFunctionalTest):
    def load_tfstate_data_from_file(self):
        tfstate_file = open(self.tfstate_path, 'r')
        tfstate_data = json.load(tfstate_file)
        self.assertIsInstance(tfstate_data, dict)

        return tfstate_data

    def test_i_can_load_a_tfstate_file(self):
        # I want to load a tfstate file and check is a valid tfstate file
        tfstate_data = self.load_tfstate_data_from_file()
        # I check that contains a version attribute
        self.assertIn('version', tfstate_data)
        # I check that contains a serial attribute
        self.assertIn('serial', tfstate_data)
        # I check that contains a modules attribute
        self.assertIn('modules', tfstate_data)

    def test_i_can_load_a_tfstate_into_object(self):
        # I want to load a tfstate file and load its contents to a Tfstate object
        tfstate = Tfstate(self.tfstate_path)
        tfstate_data = self.load_tfstate_data_from_file()
        # I want to check that the version attribute is present and matches the original data
        self.assertEqual(tfstate.version, tfstate_data['version'], 'tfstate version does not match')
        # And that the serial is present too and matches as well
        self.assertEqual(tfstate.serial, tfstate_data['serial'], 'tfstate serial does not match')
        # And that the modules attribute is a list
        self.assertIsInstance(tfstate.modules, list, 'tfstate modules attribute is not a list')


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(TfstateFileFunctionalTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
