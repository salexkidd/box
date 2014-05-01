import os
import re
import unittest
from box.findtools import find_strings

class find_strings_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.basedir = self._get_fixtures_path() 

    def test_find(self):
        strings = list(find_strings(re.compile('string\d'), 
            filename='file1', basedir=self.basedir, maxdepth=1))
        self.assertEqual(strings, ['string1'])

    def test_find_with_maxdepth_is_1(self):
        files = list(find_strings(re.compile('string\d'), 
            filename='file1', basedir=self.basedir))
        self.assertEqual(files, ['string1', 'string3'])
        
    #Protected    
        
    def _get_fixtures_path(self, *args):
        return os.path.join(os.path.dirname(__file__), 'fixtures', *args)       