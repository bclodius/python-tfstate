# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# Functional tests
from functional_tests import test_tfstate_file


def suite():
    suite = unittest.TestSuite()
    suite.addTests(test_tfstate_file.suite())
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
