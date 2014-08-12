import re
import unittest
from functools import partial
from unittest.mock import Mock, call
from box.find.find_strings import find_strings


class find_strings_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.filepathes = ['file1', 'file2']
        self.find = self._make_mock_find(self.filepathes)
        self.pfind = partial(self.find, reducers=[list])

    def test(self):
        strings = self.pfind(basedir='basedir')
        self.assertEqual(strings, ['data', 'data'])
        self.find._open.assert_has_calls(
            [call('basedir/file1'),
             call('basedir/file2')])

    def test_with_string(self):
        strings = self.pfind(string='data')
        self.assertEqual(strings, ['data', 'data'])

    def test_with_string_is_regex(self):
        strings = self.pfind(string=re.compile('data'))
        self.assertEqual(strings, ['data', 'data'])

    def test_with_string_is_regex_with_groups(self):
        strings = self.pfind(string=re.compile('(d|t)(a)'))
        self.assertEqual(strings, ['d', 'a', 't', 'a', 'd', 'a', 't', 'a'])

    def test_with_mapper(self):
        mapper = (lambda emitter:
            emitter.value(emitter.filepath + ':' + emitter.value()))
        strings = self.pfind(string='data', mappers=[mapper])
        self.assertEqual(strings, ['file1:data', 'file2:data'])

    def test_with_reducer_and_fallback(self):
        reducer = lambda values: 1 / 0
        strings = self.pfind(reducers=[reducer], fallback='fallback')
        self.assertEqual(strings, 'fallback')

    # Protected

    def _make_mock_find(self, filepathes):
        class mock_find(find_strings):
            # Protected
            _find_files = Mock(return_value=filepathes)
            # Function mock_open has different behaviour in Python 3.3/3.4:
            # In 3.3 position in "file" resets after every read()
            # In 3.4 position in "file" doesn't reset even after new open()
            # _open = mock_open(read_data='data')
            _open = Mock(return_value=Mock(
                __exit__=Mock(),
                __enter__=Mock(return_value=Mock(
                    read=Mock(return_value='data')))))
        return mock_find
