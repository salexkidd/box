import os
import unittest
from functools import partial
from box.glob import filtered_iglob

class balanced_walk_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.partial_glob = partial(
            filtered_iglob, basedir=self._basedir, sorter=sorted)

    def test(self):        
        pathes = list(self.partial_glob('*'))
        self.assertEqual(pathes, ['dir', 'file'])
        
    def test_subdir(self):        
        pathes = list(self.partial_glob('dir/*'))
        self.assertEqual(pathes, ['dir/file'])        
        
    def test_with_mode_is_files(self):
        pathes = list(self.partial_glob('*', mode='files'))
        self.assertEqual(pathes, ['file'])
        
    def test_with_mode_is_dirs(self):
        pathes = list(self.partial_glob('*', mode='dirs'))
        self.assertEqual(pathes, ['dir'])             
        
    #Protected
    
    @property
    def _basedir(self):
        return os.path.join(os.path.dirname(__file__), 'fixtures')   