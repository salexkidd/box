import os
import unittest
from box.os import balanced_walk

class balanced_walk_Test(unittest.TestCase):

    #Public
        
    def test(self):
        levels = list(balanced_walk(self._get_fixtures_path(), sorter=sorted))
        self.assertEqual(len(levels), 3)
        self.assertEqual(
            levels[0], 
            (#Dirpathes
             [self._get_fixtures_path('dir1'), 
              self._get_fixtures_path('dir2')],
             #Filepathes
             [self._get_fixtures_path('file1'), 
              self._get_fixtures_path('file2')]))
        self.assertEqual(
            levels[1], 
            (#Dirpathes
             [self._get_fixtures_path('dir1/subdir1')],
             #Filepathes
             [self._get_fixtures_path('dir1/file1'), 
              self._get_fixtures_path('dir2/file1')]))
        self.assertEqual(
            levels[2], 
            (#Dirpathes
             [],
             #Filepathes
             [self._get_fixtures_path('dir1/subdir1/file1')]))                 
        
    #Protected
    
    def _get_fixtures_path(self, *args):
        return os.path.join(os.path.dirname(__file__), 'fixtures', *args)   