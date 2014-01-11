import os
import unittest
from box.python.object_finder import ObjectFinder

class StringFinderTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.basedir = self._get_fixtures_path() 
        self.finder = ObjectFinder()

    def test_find(self):
        objects = list(self.finder.find('attr\d', 'module1.py', self.basedir))
        self.assertEqual(objects, ['attr1'])

    def test_find_with_max_depth_is_1(self):
        objects = list(self.finder.find(
            'attr\d', 'module1.py', self.basedir, max_depth=1))
        self.assertEqual(objects, ['attr1', 'attr3'])
        
    #Protected    
        
    def _get_fixtures_path(self, *args):
        return os.path.join(os.path.dirname(__file__), 'fixtures', *args)       