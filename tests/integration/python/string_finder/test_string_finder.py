import os
import unittest
from box.python.string_finder import StringFinder

class StringFinderTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.basedir = self._get_fixtures_path() 
        self.finder = StringFinder()

    def test_find(self):
        strings = list(self.finder.find('string\d', 'file1', self.basedir))
        self.assertEqual(strings, ['string1'])

    def test_find_with_max_depth_is_1(self):
        files = list(self.finder.find(
            'string\d', 'file1', self.basedir, max_depth=1))
        self.assertEqual(files, ['string1', 'string3'])
        
    #Protected    
        
    def _get_fixtures_path(self, *args):
        return os.path.join(os.path.dirname(__file__), 'fixtures', *args)       