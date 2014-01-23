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
            re.compile('(da|ta)'), 'filename', 'basedir', 'maxdepth'))
        self.assertEqual(strings, ['da', 'ta', 'da', 'ta'])
        (self.find._call_class._find_files_function.
            assert_called_with('filename', 'basedir', 'maxdepth'))        
        (self.find._call_class._open_function.
            assert_has_calls([call('file1'), call('file2')], any_order=True))
        
    def test_find_with_mapper(self):
        mapper = (lambda emitter: 
            emitter.set_value(emitter.file+':'+emitter.get_value()))
        strings = list(self.find(
            re.compile('(da|ta)'), mappers=[mapper]))
        self.assertEqual(
            strings, ['file1:da', 'file1:ta', 'file2:da', 'file2:ta'])       
    
    #Protected

    def _make_mock_find_function(self, files):
        class MockFindCall(find_strings._call_class):
            #Protected
            _open_function = mock_open(read_data='data')
            _find_files_function = Mock(return_value=files)            
        class MockFind(type(find_strings)):
            #Protected
            _call_class = MockFindCall
        mock_find = MockFind()
        return mock_find