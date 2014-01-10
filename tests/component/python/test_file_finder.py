import re
import unittest
from unittest.mock import Mock
from box.python.file_finder import FileFinder

class FileFinderTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        walk_items = [
            ['', [], ['filename1', 'filename2']],
            ['folder', [], ['filename1', 'filename2']],
            ['folder/subfolder', [], ['filename3']],
        ]
        MockFileFinder = self._make_mock_file_finder_class(walk_items)
        self.finder = MockFileFinder()

    def test_find(self):
        files = list(self.finder.find('filename1'))
        self.assertEqual(files, ['filename1'])
        
    def test_find_with_max_depth_is_1(self):
        files = list(self.finder.find('filename1', max_depth=1))
        self.assertEqual(files, ['filename1', 'folder/filename1'])
        
    def test_find_with_max_depth_is_2(self):
        files = list(self.finder.find('filename3', max_depth=2))
        self.assertEqual(files, ['folder/subfolder/filename3'])        
        
    def test_find_with_regexp(self):
        regex = re.compile('filename1+')
        files = list(self.finder.find(regex))
        self.assertEqual(files, ['filename1'])     
    
    def test_find_with_filters(self):
        filters = [lambda file: False]
        files = list(self.finder.find('filename1', filters=filters))
        self.assertEqual(files, [])
        
    def test_find_with_iterators(self):
        iterators = [lambda file: False]
        files = list(self.finder.find('filename1', iterators=iterators))
        self.assertEqual(files, [])        
          
    def test_find_with_reducers(self):
        reducers=[lambda files: list(files)[0]]
        files = self.finder.find('filename1', reducers=reducers)
        self.assertEqual(files, 'filename1')               
    
    #Protected
    
    def _make_mock_file_finder_class(self, walk_items):
        class MockFileFinder(FileFinder):
            #Protected
            _walk_operator = Mock(return_value=walk_items)
        return MockFileFinder