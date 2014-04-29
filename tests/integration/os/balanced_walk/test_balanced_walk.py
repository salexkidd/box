import os
import unittest
from box.os import balanced_walk

class balanced_walk_Test(unittest.TestCase):

    #Public

    def test_find(self):
        files = list(list(balanced_walk(self._get_fixtures_path())))
        self.assertEqual(files, [
            self._get_fixtures_path('file1'),
            self._get_fixtures_path('file2'), 
            self._get_fixtures_path('folder1', 'file1'),
            self._get_fixtures_path('folder2', 'file1'),
            self._get_fixtures_path('folder1', 'subfolder1', 'file1'),])        
        
    #Protected
    
    def _get_fixtures_path(self, *args):
        return os.path.join(os.path.dirname(__file__), 'fixtures', *args)   