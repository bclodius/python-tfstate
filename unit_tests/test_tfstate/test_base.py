# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# Python tfstate
from tfstate.base import Tfstate, Module, Resource

# Unit tests
from unit_tests.base import BaseUnitTest


class TfstateUnitTest(BaseUnitTest):
    def test_object_constructor(self):
        tfstate = Tfstate(self.tfstate_path)
        self.assertEqual(tfstate.version, tfstate.native_data['version'], 'Version attribute does not match')
        self.assertEqual(tfstate.serial, tfstate.native_data['serial'], 'Serial attribute does not match')
        modules_list = [Module(module_data) for module_data in tfstate.native_data['modules']]
        self.assertEqual(tfstate.modules, modules_list, 'Modules objects list does not match')

    def test_method_load_tfstate_data_from_file(self):
        tfstate = Tfstate(self.tfstate_path)
        # Native data are loaded in constructor, reset it for the sake of test
        tfstate.native_data = None
        self.assertIsNone(tfstate.native_data, 'Native data is not None')
        tfstate.load_tfstate_data_from_file()
        self.assertIsNotNone(tfstate.native_data, 'Native data is not loaded')


class ModuleUnitTest(BaseUnitTest):
    def test_object_constructor(self):
        tfstate = Tfstate(self.tfstate_path)
        self.assertGreaterEqual(len(tfstate.native_data['modules']), 1, 'Loaded tfstate does not contain modules')
        first_module = tfstate.native_data['modules'][0]
        tfstate_module = Module(first_module)
        self.assertEqual(tfstate_module.native_data, first_module, 'Module data loaded does not match')
        self.assertEqual(tfstate_module.path, first_module['path'], 'Module path attribute does not match')
        self.assertEqual(tfstate_module.outputs, first_module['outputs'], 'Module outputs attribute does not match')
        resources_dict = {name: Resource(name, data) for name, data in first_module['resources'].items()}
        print(resources_dict)
        print(tfstate_module.resources)
        self.assertEqual(
            tfstate_module.resources, resources_dict, 'Module resources attribute does not match')


class ResourceUnitTest(BaseUnitTest):
    def test_object_constructor(self):
        tfstate = Tfstate(self.tfstate_path)
        self.assertGreaterEqual(len(tfstate.native_data['modules']), 1, 'Loaded tfstate does not contain modules')
        module = tfstate.modules[0]
        resource = None
        for resource_name, resource_data in module.native_data['resources'].items():
            resource = Resource(resource_name, resource_data)
            self.assertEqual(resource_name, resource.name, 'Resource name does not match')
            self.assertEqual(resource_data, resource.native_data, 'Resource native data does not match')


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(TfstateUnitTest))
    suite.addTest(loader.loadTestsFromTestCase(ModuleUnitTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())