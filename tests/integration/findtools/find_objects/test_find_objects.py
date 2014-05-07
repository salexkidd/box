import os
import re
import unittest
from functools import partial
#TODO: Nose in shell imports module instead of object
from box.findtools.find_objects import find_objects

class find_objects_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.partial_find = partial(find_objects, basedir=self._make_path()) 
        
    def test_find(self):
        objects = list(self.partial_find(
            objname=re.compile('attr\d'), filename='module1.py', maxdepth=1))
        self.assertEqual(objects, ['attr1'])

    def test_find_with_maxdepth_is_1(self):
        objects = list(self.partial_find(
            objname=re.compile('attr\d'), filename='module1.py'))
        self.assertEqual(objects, ['attr1', 'attr3'])
        
    #Protected    
        
    def _make_path(self, *args):
        return os.path.join(os.path.dirname(__file__), 'fixtures', *args)       