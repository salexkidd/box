import os
import unittest
from lib31.functions.load import load

class LoaderTest(unittest.TestCase):
    
    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.path = [os.path.join(dirname, 'path')]
    
    def test_load_module(self):
        self.assertEqual(load('unittest'), 
                         load(unittest),
                         unittest)
        
    def test_load_attr(self):
        self.assertEqual(load('unittest.TestCase'), 
                         load(unittest.TestCase),
                         unittest.TestCase)
        
    def test_load_module_with_path(self):
        module = load('module', path=self.path)
        self.assertEqual(module.obj, 'obj')
        
    def test_load_attr_with_path(self):        
        attr = load('module.obj', path=self.path)
        self.assertEqual(attr, 'obj')