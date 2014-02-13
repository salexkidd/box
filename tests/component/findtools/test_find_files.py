import re
import unittest
from unittest.mock import Mock
from box.findtools.find_files import find_files

class find_files_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        walk_items = [
            ['', [], ['file1', 'file2']],
            ['folder', [], ['file1', 'file2']],
            ['folder/subfolder', [], ['file3']],
        ]
        self.find = self._make_mock_find_function(walk_items)
        
    def test(self):
        files = list(self.find(filename='file3'))
        self.assertEqual(files, ['folder/subfolder/file3']) 
        
    def test_max_depth_is_1(self):
        files = list(self.find(filename='file1', max_depth=1))
        self.assertEqual(files, ['file1'])
        
    def test_with_max_depth_is_2(self):
        files = list(self.find(filename='file1', max_depth=2))
        self.assertEqual(files, ['file1', 'folder/file1'])
        
    def test_with_regexp(self):
        regexp = re.compile('file1+')
        files = list(self.find(filename=regexp, max_depth=1))
        self.assertEqual(files, ['file1'])     
        
    def test_with_mapper(self):
        mapper = lambda emitter: emitter.value(emitter.value()+'!')
        files = list(self.find(filename='file1', mappers=[mapper]))
        self.assertEqual(files, ['file1!', 'folder/file1!'])         
          
    def test_with_reducer(self):
        reducer=lambda files: list(files)[0]
        files = self.find(filename='file1', max_depth=1, reducers=[reducer])
        self.assertEqual(files, 'file1')               
    
    #Protected
    
    def _make_mock_find_function(self, walk_items):
        class mock_find(find_files):
            #Protected
            _walk_function = Mock(return_value=walk_items)
        return mock_find