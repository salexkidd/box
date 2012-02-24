import os
import sys
import copy
import unittest
from lib31.loader import Loader
from .path.module import obj

class LoaderTest(unittest.TestCase):  
    
    def setUp(self):
        self.loader = Loader()
    
    def test_load(self):
        self.assertEqual(self.loader.load('unittest.TestCase'), 
                         self.loader.load(unittest.TestCase),
                         unittest.TestCase)
        
    def test_load_with_path(self):
        sys_path_copy = copy.copy(sys.path)
        path = [os.path.join(os.path.dirname(__file__), 'path')]
        self.assertEqual(self.loader.load('module.obj', path=path), obj)
        self.assertEqual(sys.path, sys_path_copy)