import os
import unittest
from functools import partial
from box.os.walk import enhanced_walk


class enhanced_walk_Test(unittest.TestCase):

    # Actions

    def setUp(self):
        self.pwalk = partial(
            enhanced_walk, basedir=self.basedir, sorter=sorted)

    # Helpers

    @property
    def basedir(self):
        return os.path.join(os.path.dirname(__file__), 'fixtures', 'walk')

    # Tests

    def test(self):
        levels = list(self.pwalk())
        self.assertEqual(len(levels), 3)
        self.assertEqual(levels[0],
            (# Dirpathes
             ['dir1',
              'dir2'],
             # Filepathes
             ['file1',
              'file2']))
        self.assertEqual(levels[1],
            (# Dirpathes
             ['dir1/subdir1'],
             # Filepathes
             ['dir1/file1',
              'dir2/file1']))
        self.assertEqual(levels[2],
            (# Dirpathes
             [],
             # Filepathes
             ['dir1/subdir1/file1']))

    def test_with_dirpath(self):
        levels = list(self.pwalk('dir1/subdir1'))
        self.assertEqual(len(levels), 1)
        self.assertEqual(levels[0],
            (# Dirpathes
             [],
             # Filepathes
             ['dir1/subdir1/file1']))
