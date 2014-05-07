import re
import unittest
from unittest.mock import patch
from functools import partial
from box.glob.filtered_iglob import filtered_iglob

class filtered_iglob_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        patch('glob.iglob', new=self._mock_iglob).start()
        patch('os.path.islink', new=self._mock_islink).start()
        patch('os.path.isfile', new=self._mock_isfile).start()
        patch('os.path.isdir', new=self._mock_isdir).start()
        self.addCleanup(patch.stopall)
        self.partial_glob = partial(
            filtered_iglob, sorter=sorted)

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
    
    def _mock_iglob(self, pattern):
        if pattern == '*':
            return ['dir', 'file', 'link']
        elif pattern == 'dir/*':
            return ['dir/file']
             
    def _mock_islink(self, path):
        return bool(re.search('link\d?$', path))
    
    def _mock_isfile(self, path):
        return bool(re.search('file\d?$', path))
    
    def _mock_isdir(self, path):
        return bool(re.search('dir\d?$', path))