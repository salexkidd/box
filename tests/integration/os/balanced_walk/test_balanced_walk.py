import os
import unittest
from functools import partial
from box.os import balanced_walk

class balanced_walk_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.partial_walk = partial(
            balanced_walk, basedir=self._basedir, sorter=sorted)
        
    def test(self):
        levels = list(self.partial_walk())
        self.assertEqual(len(levels), 3)
        self.assertEqual(levels[0], 
            (#Dirpathes
             ['dir1', 
              'dir2'],
             #Filepathes
             ['file1', 
              'file2']))
        self.assertEqual(levels[1], 
            (#Dirpathes
             ['dir1/subdir1'],
             #Filepathes
             ['dir1/file1', 
              'dir2/file1']))
        self.assertEqual(levels[2], 
            (#Dirpathes
             [],
             #Filepathes
             ['dir1/subdir1/file1']))
        
    def test_with_dirpath(self):
        levels = list(self.partial_walk('dir1/subdir1'))
        self.assertEqual(len(levels), 1)
        self.assertEqual(levels[0], 
            (#Dirpathes
             [],
             #Filepathes
             ['dir1/subdir1/file1']))                          
        
    #Protected
    
    @property
    def _basedir(self):
        return os.path.join(os.path.dirname(__file__), 'fixtures')