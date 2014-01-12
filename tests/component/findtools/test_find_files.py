import re
import unittest
from unittest.mock import Mock
from box.findtools.find_files import FindFiles

class FindFilesTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        walk_items = [
            ['', [], ['file1', 'file2']],
            ['folder', [], ['file1', 'file2']],
            ['folder/subfolder', [], ['file3']],
        ]
        self.find = self._make_mock_find_files_function(walk_items)

    def test_find(self):
        files = list(self.find('file1', max_depth=1))
        self.assertEqual(files, ['file1'])
        
    def test_find_with_max_depth_is_1(self):
        files = list(self.find('file1', max_depth=2))
        self.assertEqual(files, ['file1', 'folder/file1'])
        
    def test_find_with_max_depth_is_2(self):
        files = list(self.find('file3', max_depth=3))
        self.assertEqual(files, ['folder/subfolder/file3'])        
        
    def test_find_with_regexp(self):
        regexp = re.compile('file1+')
        files = list(self.find(regexp, max_depth=1))
        self.assertEqual(files, ['file1'])     
        
    def test_find_with_breaker(self):
        breaker = lambda file: True
        files = list(self.find('file1', breakers=[breaker]))
        self.assertEqual(files, [])
        
    def test_find_with_filter(self):
        fltr = lambda file: False
        files = list(self.find('file1', filters=[fltr]))
        self.assertEqual(files, [])
        
    def test_find_with_processor(self):
        processor = lambda file: 'processed_'+file
        files = list(self.find('file1', max_depth=1, processors=[processor]))
        self.assertEqual(files, [ 'processed_file1'])             
          
    def test_find_with_reducer(self):
        reducer=lambda files: list(files)[0]
        files = self.find('file1', max_depth=1, reducers=[reducer])
        self.assertEqual(files, 'file1')               
    
    #Protected
    
    def _make_mock_find_files_function(self, walk_items):
        class MockFindFiles(FindFiles):
            #Protected
            _walk_operator = Mock(return_value=walk_items)
        mock_find_files = MockFindFiles()
        return mock_find_files