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
        self.assertEqual(pathes, [])
        
    def test_with_files_is_true(self):
        pathes = list(self.partial_glob('*', files=True))
        self.assertEqual(pathes, ['file'])
        
    def test_with_dirs_is_true(self):
        pathes = list(self.partial_glob('*', dirs=True))
        self.assertEqual(pathes, ['dir'])
        
    def test_with_files_and_dirs_is_true(self):
        pathes = list(self.partial_glob('*', files=True, dirs=True))
        self.assertEqual(pathes, ['dir', 'file'])
        
    def test_with_files_and_dirs_is_true_for_subdir(self):        
        pathes = list(self.partial_glob('dir/*', files=True, dirs=True))
        self.assertEqual(pathes, ['dir/file'])               
        
    #Protected
    
    @property
    def _basedir(self):
        return os.path.join(os.path.dirname(__file__), 'fixtures')   