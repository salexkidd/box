import os
import unittest
#TODO: Nose in shell imports module instead of object
from box.findtools.find_files import find_files

class find_files_Test(unittest.TestCase):

    #Public

    def test_find(self):
        files = list(find_files(
            filename='file1', basedir=self._make_path()))
        self.assertEqual(files, [
            self._make_path('file1'), 
            self._make_path('dir1', 'file1'),
            self._make_path('dir2', 'file1'),
            self._make_path('dir1', 'subdir1', 'file1'),])

    def test_find_with_maxdepth_is_2(self):
        files = list(find_files(
            filename='file1', basedir=self._make_path(), maxdepth=2))
        self.assertEqual(files, [
            self._make_path('file1'), 
            self._make_path('dir1', 'file1'),
            self._make_path('dir2', 'file1'),])
        
    #Protected
        
    def _make_path(self, *args, basedir='fixtures'):
        return os.path.join(os.path.dirname(__file__), basedir, *args)         