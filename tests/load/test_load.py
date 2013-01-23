import os
import unittest
from lib31.load import load

class LoaderTest(unittest.TestCase):
    
    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.path = [os.path.join(dirname, 'package')]
    
    def test_load_module(self):
        self.assertEqual(
            load('unittest'), 
            load(unittest),
            unittest,
        )
        
    def test_load_attr(self):
        self.assertEqual(
            load('unittest.TestCase'), 
            load(unittest.TestCase),
            unittest.TestCase,
        )
        
    def test_load_module_with_path(self):
        self.assertRaises(
            ImportError, 
            load, 
            'unittest', 
            path=self.path,
        )

    def test_load_attr_with_path(self):
        self.assertRaises(
            ImportError,
            load,
            'unittest.TestCase', 
            path=self.path,
        )

    def test_load_module_from_path_with_path(self):
        self.assertEqual(
            load('module', path=self.path).attr, 
            'attr'
        )
        
    def test_load_attr_from_path_with_path(self):        
        self.assertEqual(
            load('module.attr', path=self.path), 
            'attr'
        )                