import os
import unittest
from box.findtools import find_files

class find_files_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.basedir = self._get_fixtures_path() 

    def test_find(self):
        files = list(find_files(
            filename='file1', basedir=self.basedir, maxdepth=1))
        self.assertEqual(files, [
            self._get_fixtures_path('file1')])

    def test_find_with_maxdepth_is_1(self):
        files = list(find_files(
            filename='file1', basedir=self.basedir))
        self.assertEqual(files, [
            self._get_fixtures_path('file1'), 
            self._get_fixtures_path('folder', 'file1')])
        
    #Protected    
        
    def _get_fixtures_path(self, *args):
        return os.path.join(os.path.dirname(__file__), 'fixtures', *args)      