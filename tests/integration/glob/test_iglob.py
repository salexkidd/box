import os
import unittest
from functools import partial
from box.glob.iglob import enhanced_iglob


class enhanced_iglob_Test(unittest.TestCase):

    # Actions

    def setUp(self):
        self.pglob = partial(
            enhanced_iglob, basedir=self.basedir, sorter=sorted)

    # Helpers

    @property
    def basedir(self):
        return os.path.join(os.path.dirname(__file__), 'fixtures', 'iglob')

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
