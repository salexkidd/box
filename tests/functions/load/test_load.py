import os
import sys
import copy
import unittest
from lib31.functions.load import load
from .path.module import obj

class LoaderTest(unittest.TestCase):  

    def test_load(self):
        self.assertEqual(load('unittest.TestCase'), 
                         load(unittest.TestCase),
                         unittest.TestCase)
        
    def test_load_with_path(self):
        sys_path_copy = copy.copy(sys.path)
        path = [os.path.join(os.path.dirname(__file__), 'path')]
        self.assertEqual(load('module.obj', path=path), obj)
        self.assertEqual(sys.path, sys_path_copy)