import os
import unittest
from functools import partial
from box.glob import filtered_iglob

class balanced_walk_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.partial_glob = partial(
            filtered_iglob, 
            sorter=sorted,
            basedir=self._get_fixtures_path())

    def test(self):
        pathes = list(self.partial_glob('*'))
        self.assertEqual(pathes, [])
        
    def test_with_files_is_true(self):
        pathes = list(self.partial_glob('*', files=True))
        self.assertEqual(pathes, [self._get_fixtures_path('file')])
        
    def test_with_dirs_is_true(self):
        pathes = list(self.partial_glob('*', dirs=True))
        self.assertEqual(pathes, [self._get_fixtures_path('dir')])
        
    def test_with_files_and_dirs_is_true(self):
        pathes = list(self.partial_glob('*', files=True, dirs=True))
        self.assertEqual(
            pathes, 
            [self._get_fixtures_path('dir'),
             self._get_fixtures_path('file')])                
        
    #Protected
    
    def _get_fixtures_path(self, *args):
        return os.path.join(os.path.dirname(__file__), 'fixtures', *args)   