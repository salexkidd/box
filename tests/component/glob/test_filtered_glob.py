import re
import unittest
from unittest.mock import patch
from box.glob.filtered_iglob import filtered_iglob

class filtered_iglob_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        patch('glob.iglob', new=self._mock_iglob).start()
        patch('os.path.join', new=self._mock_join).start()        
        patch('os.path.islink', new=self._mock_islink).start()
        patch('os.path.isfile', new=self._mock_isfile).start()
        patch('os.path.isdir', new=self._mock_isdir).start()
        self.addCleanup(patch.stopall)

    def test(self):
        pathes = list(filtered_iglob('*'))
        self.assertEqual(pathes, [])
        
    def test_with_files_is_true(self):
        pathes = list(filtered_iglob('*', files=True))
        self.assertEqual(pathes, ['file1', 'file2'])
        
    def test_with_dirs_is_true(self):
        pathes = list(filtered_iglob('*', dirs=True))
        self.assertEqual(pathes, ['dir1', 'dir2'])
        
    def test_with_files_and_dirs_is_true(self):
        pathes = list(filtered_iglob('*', files=True, dirs=True))
        self.assertEqual(pathes, ['dir1', 'dir2', 'file1', 'file2'])      
          
    #Protected
    
    def _mock_iglob(self, pattern):
        return ['dir1', 'dir2', 'file1', 'file2', 'link']
             
    def _mock_islink(self, path):
        return bool(re.search('link\d?$', path))
    
    def _mock_isfile(self, path):
        return bool(re.search('file\d?$', path))
    
    def _mock_isdir(self, path):
        return bool(re.search('dir\d?$', path))
    
    def _mock_join(self, *pathes):
        return '/'.join(pathes)