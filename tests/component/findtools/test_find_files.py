import re
import unittest
from unittest.mock import Mock
from functools import partial
from box.findtools.find_files import find_files


class find_files_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.filepathes = [
            'file1', 'file2', 'dir/file1', 'dir/file2', 'dir/subdir/file3']
        self.find = self._make_mock_find(self.filepathes)
        self.pfind = partial(self.find, reducers=[list])

    def test(self):
        files = self.pfind()
        self.assertEqual(files, self.filepathes)

    def test_with_filename(self):
        files = self.pfind(
            filters=[{'filename': 'file3'}])
        self.assertEqual(files, ['dir/subdir/file3'])

    def test_with_filename_is_regex(self):
        files = self.pfind(
            filters=[{'filename': re.compile('file1+')}, {'maxdepth': 1}])
        self.assertEqual(files, ['file1'])

    def test_with_filepath(self):
        files = self.pfind(
            filters=[{'filepath': 'file*'}])
        self.assertEqual(files, ['file1', 'file2'])

    def test_with_filepath_is_regex(self):
        files = self.pfind(
            filters=[{'filepath': re.compile('.*2$')}])
        self.assertEqual(files, ['file2', 'dir/file2'])

    def test_with_basedir(self):
        files = self.pfind(
            basedir='basedir',
            filters=[{'filename': 'file3'}])
        self.assertEqual(files, ['dir/subdir/file3'])

    def test_with_basedir_and_join(self):
        files = self.pfind(
            join=True, basedir='basedir',
            filters=[{'filename': 'file3'}])
        self.assertEqual(files, ['basedir/dir/subdir/file3'])

    def test_with_maxdepth_is_1(self):
        files = self.pfind(
            filters=[{'filename': 'file1'}, {'maxdepth': 1}])
        self.assertEqual(files, ['file1'])

    def test_with_maxdepth_is_2(self):
        files = self.pfind(
            filters=[{'filename': 'file1'}, {'maxdepth': 2}])
        self.assertEqual(files, ['file1', 'dir/file1'])

    def test_with_mapper(self):
        mapper = lambda emitter: emitter.value(emitter.value() + '!')
        files = self.pfind(
            filters=[{'filename': 'file1'}],
            mappers=[mapper])
        self.assertEqual(files, ['file1!', 'dir/file1!'])

    def test_with_reducer(self):
        reducer = lambda files: list(files)[0]
        files = self.pfind(
            filters=[{'filename': 'file1'}, {'maxdepth': 1}],
            reducers=[reducer])
        self.assertEqual(files, 'file1')

    def test_with_reducer_and_fallback(self):
        reducer = lambda values: 1 / 0
        files = self.pfind(
            reducers=[reducer], fallback='fallback')
        self.assertEqual(files, 'fallback')

    # Protected

    def _make_mock_find(self, filepathes):
        class mock_find(find_files):
            _glob = Mock(return_value=filepathes)
            _walk = Mock(return_value=filepathes)
        return mock_find
