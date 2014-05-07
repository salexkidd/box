import os
import re
import unittest
from functools import partial
#TODO: Nose in shell imports module instead of object
from box.findtools.find_strings import find_strings

class find_strings_Test(unittest.TestCase):
    
    def setUp(self):
        self.partial_find = partial(find_strings, basedir=self._make_path())    

    #Public

    def test_find(self):
        strings = list(self.partial_find(
            re.compile('string\d'), filename='file1', maxdepth=1))
        self.assertEqual(strings, ['string1'])

    def test_find_with_maxdepth_is_1(self):
        files = list(self.partial_find(
            re.compile('string\d'), filename='file1'))
        self.assertEqual(files, ['string1', 'string3'])
        
    #Protected    
        
    def _make_path(self, *args, basedir='fixtures'):
        return os.path.join(os.path.dirname(__file__), basedir, *args)       