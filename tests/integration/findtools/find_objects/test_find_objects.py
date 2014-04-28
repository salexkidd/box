import os
import re
import unittest
from box.findtools import find_objects

class find_objects_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.basedir = self._get_fixtures_path() 

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
        
    def _get_fixtures_path(self, *args):
        return os.path.join(os.path.dirname(__file__), 'fixtures', *args)       