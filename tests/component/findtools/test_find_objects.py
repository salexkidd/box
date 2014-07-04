import re
import unittest
from functools import partial
from unittest.mock import Mock, call, patch
from box.findtools.find_objects import find_objects

class find_objects_Test(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.find = self._make_mock_find()
        self.pfind = partial(self.find, files=['file1', 'file2'])
        
    def test(self):
        objects = list(self.pfind(basedir='basedir'))
        self.assertTrue(objects)
        self.find._loader_class.assert_has_calls(
            [call('basedir/file1', 'basedir/file1'), 
             call('basedir/file2', 'basedir/file2')])
        self.find._loader_class.return_value.load_module.assert_has_calls(
            [call('basedir/file1'), 
             call('basedir/file2')])
        
    @patch.object(find_objects, '_find_files')    
    def test_without_files(self, find_files):
        find_files.return_value = ['file1', 'file2']
        objects = list(self.find(
            basedir='basedir',
            filename='filename',
            notfilename='notfilename',
            filepath='filepath',
            notfilepath='notfilepath',
            maxdepth='maxdepth',
            onwalkerror='onwalkerror'))
        self.assertTrue(objects)
        find_files.assert_called_with(
            basedir='basedir',
            filename='filename',
            notfilename='notfilename',
            filepath='filepath',
            notfilepath='notfilepath',
            maxdepth='maxdepth',
            onwalkerror='onwalkerror')        
        
    def test_with_objname(self):
        objects = list(self.pfind(objname='call'))
        self.assertEqual(objects, [call, call])
        
    def test_with_objname_is_regex(self):
        objects = list(self.pfind(objname=re.compile('call')))
        self.assertEqual(objects, [call, call])        
        
    def test_with_objtype(self):
        objects = list(self.pfind(objtype=type(call)))
        self.assertEqual(objects, [call, call])
        
    def test_with_objtype_is_list(self):
        objects = list(self.pfind(objtype=[type(call)]))
        self.assertEqual(objects, [call, call])             
        
    def test_with_mapper(self):
        mapper = lambda emitter: emitter.emit(emitter.objtype)
        objects = list(self.pfind(objname='call', mappers=[mapper]))
        self.assertEqual(objects, [type(call), type(call)])
        
    def test_with_reducer_and_fallback(self):
        reducer = lambda values: 1/0
        objects = self.pfind(reducers=[reducer], fallback='fallback')
        self.assertEqual(objects, 'fallback')
        
    #Protected

    def _make_mock_find(self):
        class mock_find(find_objects):
            #Protected
            _loader_class = Mock(return_value=Mock(
                load_module=Mock(return_value=unittest.mock)))
        return mock_find