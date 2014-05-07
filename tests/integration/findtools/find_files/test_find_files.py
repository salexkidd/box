import os
import unittest
from functools import partial
#TODO: Nose in shell imports module instead of object
from box.findtools.find_files import find_files

class find_files_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.partial_find = partial(find_files, basedir=self._make_path())

    def test_find(self):
        files = list(self.partial_find(filename='file1'))
        self.assertEqual(files, [
            self._make_path('file1'), 
            self._make_path('dir1', 'file1'),
            self._make_path('dir2', 'file1'),
            self._make_path('dir1', 'subdir1', 'file1'),])

    def test_find_with_maxdepth_is_2(self):
        files = list(self.partial_find(filename='file1', maxdepth=2))
        self.assertEqual(files, [
            self._make_path('file1'), 
            self._make_path('dir1', 'file1'),
            self._make_path('dir2', 'file1'),])
    
    @unittest.skip    
    def test_find_with_filepath(self):
        files = list(self.partial_find(filepath='file1'))
        self.assertEqual(files, [
            self._make_path('file1')])        
        
    #Protected
        
    def _make_path(self, *args, basedir='fixtures'):
        return os.path.join(os.path.dirname(__file__), basedir, *args)         