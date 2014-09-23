import os
import unittest
from importlib import import_module
component = import_module('box.importlib.file')


class import_object_Test(unittest.TestCase):

    # Tests

    def test(self):
        filepath = os.path.join(os.path.dirname(__file__), 'test_object.py')
        module = component.import_file(filepath)
        self.assertIs(module.unittest, unittest)
