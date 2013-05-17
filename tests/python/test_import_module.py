import os
import unittest
from lib31.python import import_module

class ImportModuleTest(unittest.TestCase):
    
    def test_import_module(self):
        self.assertEqual(
            import_module('unittest'), 
            unittest,
        )             