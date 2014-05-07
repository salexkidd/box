import os
import re
import unittest
#TODO: Nose in shell imports module instead of object
from box.findtools.find_objects import find_objects

class find_objects_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.basedir = self._make_path() 

    def test_find(self):
        objects = list(find_objects(
            objname=re.compile('attr\d'), 
            filename='module1.py', 
            basedir=self.basedir, 
            maxdepth=1))
        self.assertEqual(objects, ['attr1'])

    def test_find_with_maxdepth_is_1(self):
        objects = list(find_objects(
            objname=re.compile('attr\d'), 
            filename='module1.py', 
            basedir=self.basedir))
        self.assertEqual(objects, ['attr1', 'attr3'])
        
    #Protected    
        
    def _make_path(self, *args, basedir='fixtures'):
        return os.path.join(os.path.dirname(__file__), basedir, *args)       