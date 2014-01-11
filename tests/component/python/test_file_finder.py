import re
import unittest
from unittest.mock import Mock
from box.python.file_finder import FileFinder

class FileFinderTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        walk_items = [
            ['', [], ['file1', 'file2']],
            ['folder', [], ['file1', 'file2']],
            ['folder/subfolder', [], ['file3']],
        ]
        MockFileFinder = self._make_mock_file_finder_class(walk_items)
        self.finder = MockFileFinder()

    def test_find(self):
        files = list(self.finder.find('file1'))
        self.assertEqual(files, ['file1'])
        
    def test_find_with_max_depth_is_1(self):
        files = list(self.finder.find('file1', max_depth=1))
        self.assertEqual(files, ['file1', 'folder/file1'])
        
    def test_find_with_max_depth_is_2(self):
        files = list(self.finder.find('file3', max_depth=2))
        self.assertEqual(files, ['folder/subfolder/file3'])        
        
    def test_find_with_regexp(self):
        regexp = re.compile('file1+')
        files = list(self.finder.find(regexp))
        self.assertEqual(files, ['file1'])     
        
    def test_find_with_breaker(self):
        breaker = lambda file: True
        files = list(self.finder.find('file1', breakers=[breaker]))
        self.assertEqual(files, [])
        
    def test_find_with_filter(self):
        fltr = lambda file: False
        files = list(self.finder.find('file1', filters=[fltr]))
        self.assertEqual(files, [])
        
    def test_find_with_processor(self):
        processor = lambda file: 'processed_'+file
        files = list(self.finder.find('file1', processors=[processor]))
        self.assertEqual(files, [ 'processed_file1'])             
          
    def test_find_with_reducer(self):
        reducer=lambda files: list(files)[0]
        files = self.finder.find('file1', reducers=[reducer])
        self.assertEqual(files, 'file1')               
    
    #Protected
    
    def _make_mock_file_finder_class(self, walk_items):
        class MockFileFinder(FileFinder):
            #Protected
            _walk_operator = Mock(return_value=walk_items)
        return MockFileFinder