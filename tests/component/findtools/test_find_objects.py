import re
import unittest
from functools import partial
from unittest.mock import Mock, call
from box.findtools.find_objects import find_objects


class find_objects_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.filepathes = ['file1', 'file2']
        self.find = self._make_mock_find(self.filepathes)
        self.pfind = partial(self.find, reducers=[list])

    def test(self):
        objects = self.pfind(basedir='basedir')
        self.assertTrue(objects)
        # Check SourceFileLoader call
        self.find._SourceFileLoader.assert_has_calls(
            [call('basedir/file1', 'basedir/file1'),
             call('basedir/file2', 'basedir/file2')])
        # Check SourceFileLoader's return_value (loader) load_module call
        self.find._SourceFileLoader.return_value.load_module.assert_has_calls(
            [call('basedir/file1'),
             call('basedir/file2')])

    def test_with_objname(self):
        objects = self.pfind({'objname': 'call'})
        self.assertEqual(objects, [call, call])

    def test_with_objname_is_regex(self):
        objects = self.pfind({'objname': re.compile('^call')})
        self.assertEqual(objects, [call, call])

    def test_with_objtype(self):
        objects = self.pfind({'objtype': type(call)})
        self.assertEqual(objects, [call, call])

    def test_with_objtype_is_list(self):
        objects = self.pfind({'objtype': [type(call)]})
        self.assertEqual(objects, [call, call])

    def test_with_mapper(self):
        mapper = lambda emitter: emitter.emit(emitter.objtype)
        objects = self.pfind({'objname': 'call'}, mappers=[mapper])
        self.assertEqual(objects, [type(call), type(call)])

    def test_with_reducer_and_fallback(self):
        reducer = lambda values: 1 / 0
        objects = self.pfind(reducers=[reducer], fallback='fallback')
        self.assertEqual(objects, 'fallback')

    # Protected

    def _make_mock_find(self, filepathes):
        class mock_find(find_objects):
            # Protected
            _find_files = Mock(return_value=filepathes)
            _SourceFileLoader = Mock(return_value=Mock(
                load_module=Mock(return_value=unittest.mock)))
        return mock_find
