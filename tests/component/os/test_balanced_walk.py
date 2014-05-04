import os
import re
import unittest
from unittest.mock import Mock, patch
from box.os.balanced_walk import balanced_walk

class balanced_walk_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        patch('os.listdir', new=self._mock_listdir).start()
        patch('os.path.islink', new=self._mock_islink).start()
        patch('os.path.isfile', new=self._mock_isfile).start()
        patch('os.path.isdir', new=self._mock_isdir).start()
        patch('os.path.join', new=self._mock_join).start()
        self.addCleanup(patch.stopall)
        self.error = os.error()

    def test(self):
        files = list(balanced_walk('fixtures'))
        self.assertEqual(files, [
            'fixtures/file1',
            'fixtures/file2', 
            'fixtures/dir1/file1',
            'fixtures/dir2/file1',
            'fixtures/dir1/subdir1/file1',])
        
    def test_raise_error_with_onerror(self):
        onerror = Mock()
        files = list(balanced_walk('error', onerror=onerror))
        self.assertEqual(files, [])
        onerror.assert_called_with(self.error)
        
    #Protected
   
    def _mock_listdir(self, path):
        if path == 'fixtures':
            return ['dir1', 'dir2', 'file1', 'file2', 'link']
        elif path == 'fixtures/dir1':
            return ['subdir1', 'file1',]
        elif path == 'fixtures/dir2':
            return ['file1',]
        elif path == 'fixtures/dir1/subdir1':
            return ['file1']
        elif path == 'error':
            raise self.error      
    
    def _mock_islink(self, path):
        return bool(re.search('link\d?$', path))

    def _mock_isfile(self, path):
        return bool(re.search('file\d?$', path))
    
    def _mock_isdir(self, path):
        return bool(re.search('dir\d?$', path))
    
    def _mock_join(self, *pathes):
        return '/'.join(pathes)