import unittest
from unittest.mock import Mock, call
from box.findtools.find_objects import find_objects

class find_objects_Test(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        files = ['file1', 'file2']
        self.find = self._make_mock_find_function(files)
        
    def test_find(self):
        objects = list(self.find(
            objname='call', 
            filename='filename', 
            basedir='basedir', 
            max_depth='max_depth'))
        self.assertEqual(objects, [call, call])
        self.find._find_files_function.assert_called_with(
            file=None,
            filename='filename', 
            basedir='basedir', 
            max_depth='max_depth')
        (self.find._source_file_loader_class.
            assert_has_calls([call('file1', 'file1'), call('file2', 'file2')]))
        (self.find._source_file_loader_class.return_value.load_module.
            assert_has_calls([call('file1'), call('file2')]))
        
    def test_find_with_mapper(self):
        mapper = lambda emitter: emitter.emit(emitter.objname)
        objects = list(self.find(objname='call', mappers=[mapper]))
        self.assertEqual(objects, ['call', 'call'])               
    
    #Protected

    def _make_mock_find_function(self, files):
        class mock_find(find_objects):
            #Protected
            _source_file_loader_class = Mock(return_value=Mock(
                load_module=Mock(return_value=unittest.mock)))
            _find_files_function = Mock(return_value=files)
        return mock_find