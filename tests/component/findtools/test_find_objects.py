import unittest
from unittest.mock import Mock, call
from box.findtools.find_objects import find_objects

class find_objects_Test(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        files = ['file1', 'file2']
        self.find = self._make_mock_find_function(files)
        
    def test(self):
        objects = list(self.find(
            filename='filename', 
            filepath='filepath',             
            basedir='basedir', 
            maxdepth='maxdepth'))
        self.assertTrue(objects)
        self.find._find_files_function.assert_called_with(
            filename='filename',
            filepath='filepath',              
            basedir='basedir', 
            maxdepth='maxdepth')
        (self.find._source_file_loader_class.
            assert_has_calls([call('file1', 'file1'), call('file2', 'file2')]))
        (self.find._source_file_loader_class.return_value.load_module.
            assert_has_calls([call('file1'), call('file2')]))
        
    def test_with_objname(self):
        objects = list(self.find(objname='call'))
        self.assertEqual(objects, [call, call])
        
    def test_with_objtype(self):
        objects = list(self.find(objtype=type(call)))
        self.assertEqual(objects, [call, call])
        
    def test_with_objtype_list(self):
        objects = list(self.find(objtype=[type(call)]))
        self.assertEqual(objects, [call, call])             
        
    def test_with_mapper(self):
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