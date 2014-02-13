import re
import unittest
from unittest.mock import Mock, mock_open, call
from box.findtools.find_strings import find_strings

class find_strings_Test(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        files = ['file1', 'file2']
        self.find = self._make_mock_find_function(files)
        
    def test_find(self):
        strings = list(self.find(
            filename='filename', 
            basedir='basedir', 
            max_depth='max_depth'))
        self.assertEqual(strings, ['data', 'data'])
        self.find._find_files_function.assert_called_with(
            file=None,
            filename='filename', 
            basedir='basedir', 
            max_depth='max_depth')    
        self.find._open_function.assert_has_calls(
            [call('file1'), call('file2')], any_order=True)
        
    def test_find_with_string(self):
        strings = list(self.find(re.compile('(da|ta)')))
        self.assertEqual(strings, ['da', 'ta', 'da', 'ta'])       
        
    def test_find_with_mapper(self):
        mapper = (lambda emitter: 
            emitter.value(emitter.file+':'+emitter.value()))
        strings = list(self.find(re.compile('(da|ta)'), mappers=[mapper]))
        self.assertEqual(strings, 
            ['file1:da', 'file1:ta', 'file2:da', 'file2:ta'])       
    
    #Protected

    def _make_mock_find_function(self, files):
        class mock_find(find_strings):
            #Protected
            _open_function = mock_open(read_data='data')
            _find_files_function = Mock(return_value=files)
        return mock_find