import re
import unittest
from unittest.mock import patch
from functools import partial
from importlib import import_module
component = import_module('box.glob.iglob')


class enhanced_iglob_Test(unittest.TestCase):

    # Actions

    def setUp(self):
        self.addCleanup(patch.stopall)
        patch.object(component, 'iglob', new=self._mock_iglob).start()
        patch.object(component.os.path, 'islink', new=self._mock_islink).start()
        patch.object(component.os.path, 'isfile', new=self._mock_isfile).start()
        patch.object(component.os.path, 'isdir', new=self._mock_isdir).start()
        self.pglob = partial(component.enhanced_iglob, sorter=sorted)

    # Helpers

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

    # Tests

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
