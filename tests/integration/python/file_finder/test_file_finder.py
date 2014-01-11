import os
import unittest
from box.python.file_finder import FileFinder

class FileFinderTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.basedir = self._get_fixtures_path() 
        self.finder = FileFinder()

    def test_find(self):
        files = list(self.finder.find('file1', self.basedir))
        self.assertEqual(files, [
            self._get_fixtures_path('file1')])

    def test_find_with_max_depth_is_1(self):
        files = list(self.finder.find('file1', self.basedir, max_depth=1))
        self.assertEqual(files, [
            self._get_fixtures_path('file1'), 
            self._get_fixtures_path('folder', 'file1')])
        
    #Protected    
        
    def _get_fixtures_path(self, *args):
        return os.path.join(os.path.dirname(__file__), 'fixtures', *args)      