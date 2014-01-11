import unittest
from unittest.mock import Mock, mock_open, call
from box.python.string_finder import StringFinder, StringFinderFileFinderReducer

class StringFinderTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        files = ['file1', 'file2']
        MockStringFinder = self._make_mock_string_finder_class(files)
        self.finder = MockStringFinder()
        
    def test_find(self):
        strings = self.finder.find('pattern', 
            filename='filename', 
            basedir='basedir', 
            max_depth='max_depth', 
            breakers='breakers', 
            filters='filters', 
            processors='processors', 
            reducers='reducers')
        self.assertEqual(strings, ['strings'])
        self.finder._file_finder_class.assert_called_with()
        self.finder._file_finder_reducer_class.assert_called_with(
            'pattern', 'breakers', 'filters', 'processors', 'reducers')
        self.finder._file_finder_class.return_value.find.assert_called_with(
            'filename', 'basedir', 'max_depth', reducers=['reducer'])
    
    #Protected

    def _make_mock_string_finder_class(self, files):
        class MockStringFinder(StringFinder):
            #Protected
            _file_finder_class = Mock(return_value=Mock(
                find=Mock(return_value=['strings'])))
            _file_finder_reducer_class = Mock(return_value='reducer')
        return MockStringFinder
    

class StringFinderFileFinderReducerTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.Reducer = self._make_mock_reducer_class()
        self.files = ['file1', 'file2']
        
    def test___call__(self):
        reducer = self.Reducer('(da|ta)')
        strings = list(reducer(self.files))
        self.assertEqual(strings, ['da', 'ta', 'da', 'ta'])
        reducer._open_operator.assert_has_calls([
            call('file1'), call('file2')], any_order=True)
        
    def test___call___with_processor(self):
        processor = lambda string, file: file+':'+string
        reducer = self.Reducer('(da|ta)', processors=[processor])
        strings = list(reducer(self.files))
        self.assertEqual(
            strings, ['file1:da', 'file1:ta', 'file2:da', 'file2:ta'])       
    
    #Protected
    
    def _make_mock_reducer_class(self):
        class MockReducer(StringFinderFileFinderReducer):
            #Protected
            _open_operator = mock_open(read_data='data')
        return MockReducer