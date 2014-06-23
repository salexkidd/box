import os
import re
import unittest
from functools import partial
#TODO: Nose in shell imports module instead of object
from box.findtools.find_strings import find_strings

class find_strings_Test(unittest.TestCase):
    
    def setUp(self):
        self.pfind = partial(find_strings, basedir=self._basedir)

    #Public

    def test_find(self):
        strings = list(self.pfind(
                re.compile('string\d'), 
                filename='file1'))        
        self.assertEqual(strings, ['string1', 'string3'])
        
    def test_find_with_maxdepth_is_1(self):
        strings = list(self.pfind(
                re.compile('string\d'), 
                filename='file1', 
                maxdepth=1))         
        self.assertEqual(strings, ['string1'])
        
    #Protected    
        
    @property    
    def _basedir(self):
        return os.path.join(os.path.dirname(__file__), 'fixtures')       