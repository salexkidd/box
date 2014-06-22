import os
import re
import unittest
from functools import partial
#TODO: Nose in shell imports module instead of object
from box.findtools.find_files import find_files
from box.findtools.find_strings import find_strings

class find_strings_Test(unittest.TestCase):
    
    def setUp(self):
        self.pfind_files = partial(find_files, basedir=self._basedir, join=True)

    #Public

    def test_find(self):
        files = list(self.pfind_files(filename='file1'))
        strings = list(find_strings(re.compile('string\d'), files=files))        
        self.assertEqual(strings, ['string1', 'string3'])
        
    def test_find_with_maxdepth_is_1(self):
        files = list(self.pfind_files(filename='file1', maxdepth=1))
        strings = list(find_strings(re.compile('string\d'), files=files))
        self.assertEqual(strings, ['string1'])
        
    #Protected    
        
    @property    
    def _basedir(self):
        return os.path.join(os.path.dirname(__file__), 'fixtures')       