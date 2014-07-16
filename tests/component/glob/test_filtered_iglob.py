import re
import unittest
from unittest.mock import patch
from functools import partial
from box.glob.filtered_iglob import filtered_iglob

class filtered_iglob_Test(unittest.TestCase):

    # Public

    def setUp(self):
        patch('glob.iglob', new=self._mock_iglob).start()
        patch('os.path.islink', new=self._mock_islink).start()
        patch('os.path.isfile', new=self._mock_isfile).start()
        patch('os.path.isdir', new=self._mock_isdir).start()
        self.addCleanup(patch.stopall)
        self.pglob = partial(filtered_iglob, sorter=sorted)

    def test(self):
        pathes = list(self.pglob('*'))
        self.assertEqual(pathes, ['dir', 'file'])

    def test_subdir(self):
        pathes = list(self.pglob('dir/*'))
        self.assertEqual(pathes, ['dir/file'])

    def test_with_mode_is_files(self):
        pathes = list(self.pglob('*', mode='files'))
        self.assertEqual(pathes, ['file'])

    def test_with_mode_is_dirs(self):
        pathes = list(self.pglob('*', mode='dirs'))
        self.assertEqual(pathes, ['dir'])

    # Protected

    def _mock_iglob(self, pattern):
        if pattern == '*':
            return ['dir', 'file', 'link']
        elif pattern == 'dir/*':
            return ['dir/file']

    def _mock_islink(self, path):
        return bool(re.search('link\d?$', path))

    def _mock_isfile(self, path):
        return bool(re.search('file\d?$', path))

    def _mock_isdir(self, path):
        return bool(re.search('dir\d?$', path))
