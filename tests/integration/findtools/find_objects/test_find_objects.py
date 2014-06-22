import os
import re
import unittest
from functools import partial
#TODO: Nose in shell imports module instead of object
from box.findtools.find_files import find_files
from box.findtools.find_objects import find_objects

class find_objects_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.pfind_files = partial(find_files, basedir=self._basedir, join=True)

    def test_find(self):
        files = list(self.pfind_files(filename='module1.py'))
        objects = list(find_objects(objname=re.compile('attr\d'), files=files))
        self.assertEqual(objects, ['attr1', 'attr3'])
        
    def test_find_with_maxdepth_is_1(self):
        files = list(self.pfind_files(filename='module1.py', maxdepth=1))
        objects = list(find_objects(objname=re.compile('attr\d'), files=files)) 
        self.assertEqual(objects, ['attr1'])
        
    #Protected    
        
    @property    
    def _basedir(self):
        return os.path.join(os.path.dirname(__file__), 'fixtures')       