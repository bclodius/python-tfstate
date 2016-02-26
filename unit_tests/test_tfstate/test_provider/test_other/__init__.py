# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# Unit tests
from unit_tests.test_tfstate.test_provider.test_other import test_null_resource


def suite():
    suite = unittest.TestSuite()
    suite.addTests(test_null_resource.suite())
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
