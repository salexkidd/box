import os
import unittest
from functools import partial
# TODO: Nose in shell imports module instead of object
from box.findtools.find_files import find_files


# TODO: remove explicit "/" usage
class find_files_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.pfind = partial(find_files, basedir=self._basedir)

    def test_find(self):
        files = list(self.pfind())
        self.assertEqual(files,
            ['file1',
             'file2',
             'dir1/file1',
             'dir2/file1',
             'dir1/subdir1/file1'])

    def test_find_with_filename(self):
        files = list(self.pfind({'filename': 'file1'}))
        self.assertEqual(files,
            ['file1',
             'dir1/file1',
             'dir2/file1',
             'dir1/subdir1/file1'])

    def test_find_with_filename_and_with_maxdepth_is_2(self):
        files = list(self.pfind({'filename': 'file1'}, {'maxdepth': 2}))
        self.assertEqual(files,
            ['file1',
             'dir1/file1',
             'dir2/file1'])

    def test_find_with_filepathes(self):
        files = list(self.pfind(filepathes=['file1']))
        self.assertEqual(files,
            ['file1'])

    def test_find_with_filepath_wildcard(self):
        files = list(self.pfind(filepathes=['dir*/file*']))
        self.assertEqual(files,
            ['dir1/file1',
             'dir2/file1', ])

    # Protected

    @property
    def _basedir(self):
        return os.path.join(os.path.dirname(__file__), 'fixtures')
