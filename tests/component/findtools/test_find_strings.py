import re
import unittest
from unittest.mock import Mock, mock_open, call
from box.findtools.find_strings import FindStrings

class FindStringsTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        files = ['file1', 'file2']
        self.find = self._make_mock_find_strings_function(files)
        
    def test_find(self):
        strings = list(self.find(
            re.compile('(da|ta)'), 'filename', 'basedir', 'maxdepth'))
        self.assertEqual(strings, ['da', 'ta', 'da', 'ta'])
        (self.find._find_files_function.
            assert_called_with('filename', 'basedir', 'maxdepth'))        
        (self.find._open_function.
            assert_has_calls([call('file1'), call('file2')], any_order=True))
        
    def test_find_with_processor(self):
        processor = lambda string, file: file+':'+string
        strings = list(self.find(
            re.compile('(da|ta)'), processors=[processor]))
        self.assertEqual(
            strings, ['file1:da', 'file1:ta', 'file2:da', 'file2:ta'])       
    
    #Protected

    def _make_mock_find_strings_function(self, files):
        class MockFindStrings(FindStrings):
            #Protected
            _open_function = mock_open(read_data='data')
            _find_files_function = Mock(return_value=files)
        mock_find_strings = MockFindStrings()
        return mock_find_strings