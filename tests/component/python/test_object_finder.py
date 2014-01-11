import unittest
from unittest.mock import Mock, call
from box.python.object_finder import ObjectFinder

class ObjectFinderTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        files = ['file1', 'file2']
        MockObjectFinder = self._make_mock_object_finder_class(files)
        self.finder = MockObjectFinder()
        
    def test_find(self):
        objects = list(self.finder.find('call', 
            'filename', 'basedir', 'maxdepth'))
        self.assertEqual(objects, [call, call])
        (self.finder._file_finder_class.return_value.find.
            assert_called_with('filename', 'basedir', 'maxdepth'))
        (self.finder._source_file_loader_class.
            assert_has_calls([call('file1', 'file1'), call('file2', 'file2')]))
        (self.finder._source_file_loader_class.return_value.load_module.
            assert_has_calls([call('file1'), call('file2')]))
        
    def test_find_with_processor(self):
        processor = lambda obj, name, module: name
        objects = list(self.finder.find('call', processors=[processor]))
        self.assertEqual(objects, ['call', 'call'])               
    
    #Protected

    def _make_mock_object_finder_class(self, files):
        class MockObjectFinder(ObjectFinder):
            #Protected
            _source_file_loader_class = Mock(return_value=Mock(
                load_module=Mock(return_value=unittest.mock)))
            _file_finder_class = Mock(return_value=Mock(
                find=Mock(return_value=files)))
        return MockObjectFinder