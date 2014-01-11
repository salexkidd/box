import unittest
from unittest.mock import Mock, mock_open, call
from box.python.string_finder import StringFinder

class StringFinderTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        files = ['file1', 'file2']
        MockStringFinder = self._make_mock_string_finder_class(files)
        self.finder = MockStringFinder()
        
    def test_find(self):
        strings = list(self.finder.find('(da|ta)', 
            'filename', 'basedir', 'maxdepth'))
        self.assertEqual(strings, ['da', 'ta', 'da', 'ta'])
        (self.finder._file_finder_class.return_value.find.
            assert_called_with('filename', 'basedir', 'maxdepth'))        
        (self.finder._open_operator.
            assert_has_calls([call('file1'), call('file2')], any_order=True))
        
    def test_find_with_processor(self):
        processor = lambda string, file: file+':'+string
        strings = list(self.finder.find('(da|ta)', processors=[processor]))
        self.assertEqual(
            strings, ['file1:da', 'file1:ta', 'file2:da', 'file2:ta'])       
    
    #Protected

    def _make_mock_string_finder_class(self, files):
        class MockStringFinder(StringFinder):
            #Protected
            _open_operator = mock_open(read_data='data')
            _file_finder_class = Mock(return_value=Mock(
                find=Mock(return_value=files)))
        return MockStringFinder