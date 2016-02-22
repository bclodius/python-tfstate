# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# Python tfstate
from tfstate.base import Tfstate

# Unit tests
from unit_tests.base import BaseUnitTest


class TfstateUnitTest(BaseUnitTest):
    def test_method_load_tfstate_data_from_file(self):
        tfstate = Tfstate(self.tfstate_path)
        # Native data are loaded in constructor, reset it for the sake of test
        tfstate.native_data = None
        self.assertIsNone(tfstate.native_data, 'Native data is not None')
        tfstate.load_tfstate_data_from_file()
        self.assertIsNotNone(tfstate.native_data, 'Native data is not loaded')


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(TfstateUnitTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
