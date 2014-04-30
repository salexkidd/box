import re
import unittest
from unittest.mock import Mock, call
from box.findtools.find_strings import find_strings

class find_strings_Test(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        files = ['file1', 'file2']
        self.find = self._make_mock_find_function(files)
        
    def test(self):
        strings = list(self.find(
            filename='filename',
            filepath='filepath',
            basedir='basedir', 
            maxdepth='maxdepth',
            onwalkerror='onwalkerror'))
        self.assertEqual(strings, ['data', 'data'])
        self.find._find_files_function.assert_called_with(
            filename='filename',
            filepath='filepath',            
            basedir='basedir', 
            maxdepth='maxdepth',
            onwalkerror='onwalkerror')    
        self.find._open_function.assert_has_calls(
            [call('file1'), call('file2')], any_order=True)
    
    def test_with_string(self):
        strings = list(self.find('data'))
        self.assertEqual(strings, ['data', 'data'])
        
    def test_with_string_is_regex(self):
        strings = list(self.find(re.compile('(da|ta)')))
        self.assertEqual(strings, ['da', 'ta', 'da', 'ta'])       
        
    def test_with_mapper(self):
        mapper = (lambda emitter: 
            emitter.value(emitter.filepath+':'+emitter.value()))
        strings = list(self.find(re.compile('(da|ta)'), mappers=[mapper]))
        self.assertEqual(strings, 
            ['file1:da', 'file1:ta', 'file2:da', 'file2:ta'])
    
    def test_with_reducer_and_fallback(self):
        reducer = lambda values: 1/0
        strings = self.find(reducers=[reducer], fallback='fallback')
        self.assertEqual(strings, 'fallback')          
    
    #Protected

    def _make_mock_find_function(self, files):
        class mock_find(find_strings):
            #Protected
            #Function mock_open has different behaviour in Python 3.3/3.4:
            #In 3.3 position in "file" resets after every read()
            #In 3.4 position in "file" doesn't reset even after new open()
            #_open_function = mock_open(read_data='data')
            _open_function = Mock(return_value=Mock(
                __exit__=Mock(),
                __enter__=Mock(return_value=Mock(
                    read=Mock(return_value='data')))))
            _find_files_function = Mock(return_value=files)
        return mock_find