# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# Unit tests
from unit_tests.test_tfstate.test_provider.test_aws import test_base, test_aws_eip, test_aws_internet_gateway
from unit_tests.test_tfstate.test_provider.test_aws import test_aws_route_table, test_aws_route_table_association
from unit_tests.test_tfstate.test_provider.test_aws import test_aws_subnet, test_aws_vpc, test_aws_key_pair
from unit_tests.test_tfstate.test_provider.test_aws import test_aws_instance, test_aws_autoscaling_notification


def suite():
    suite = unittest.TestSuite()
    suite.addTests(test_base.suite())
    suite.addTests(test_aws_eip.suite())
    suite.addTests(test_aws_internet_gateway.suite())
    suite.addTests(test_aws_route_table.suite())
    suite.addTests(test_aws_route_table_association.suite())
    suite.addTests(test_aws_subnet.suite())
    suite.addTests(test_aws_vpc.suite())
    suite.addTests(test_aws_key_pair.suite())
    suite.addTests(test_aws_instance.suite())
    suite.addTest(test_aws_autoscaling_notification.suite())
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
