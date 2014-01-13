import unittest
from unittest.mock import Mock, call
from box.findtools.find_objects import FindObjects

class FindObjectsTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        files = ['file1', 'file2']
        self.find = self._make_mock_find_objects_function(files)
        
    def test_find(self):
        objects = list(self.find('call', 
            'filename', 'basedir', 'maxdepth'))
        self.assertEqual(objects, [call, call])
        (self.find._find_files_function.
            assert_called_with('filename', 'basedir', 'maxdepth'))
        (self.find._source_file_loader_class.
            assert_has_calls([call('file1', 'file1'), call('file2', 'file2')]))
        (self.find._source_file_loader_class.return_value.load_module.
            assert_has_calls([call('file1'), call('file2')]))
        
    def test_find_with_processor(self):
        processor = lambda obj, name, module: name
        objects = list(self.find('call', processors=[processor]))
        self.assertEqual(objects, ['call', 'call'])               
    
    #Protected

    def _make_mock_find_objects_function(self, files):
        class MockFindObjects(FindObjects):
            #Protected
            _source_file_loader_class = Mock(return_value=Mock(
                load_module=Mock(return_value=unittest.mock)))
            _find_files_function = Mock(return_value=files)
        mock_find_object = MockFindObjects()
        return mock_find_object