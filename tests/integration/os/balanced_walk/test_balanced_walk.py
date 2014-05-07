import os
import unittest
from box.os import balanced_walk

class balanced_walk_Test(unittest.TestCase):

    #Public
        
    def test(self):
        levels = list(balanced_walk(self._make_path(), sorter=sorted))
        self.assertEqual(len(levels), 3)
        self.assertEqual(levels[0], 
            (#Dirpathes
             [self._make_path('dir1'), 
              self._make_path('dir2')],
             #Filepathes
             [self._make_path('file1'), 
              self._make_path('file2')]))
        self.assertEqual(levels[1], 
            (#Dirpathes
             [self._make_path('dir1/subdir1')],
             #Filepathes
             [self._make_path('dir1/file1'), 
              self._make_path('dir2/file1')]))
        self.assertEqual(levels[2], 
            (#Dirpathes
             [],
             #Filepathes
             [self._make_path('dir1/subdir1/file1')]))                 
        
    #Protected
    
    def _make_path(self, *args, basedir='fixtures'):
        return os.path.join(os.path.dirname(__file__), basedir, *args)    