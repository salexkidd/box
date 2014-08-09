import os
import re
import unittest
from functools import partial
# TODO: Nose in shell imports module instead of object
from box.findtools.find_strings import find_strings


class find_strings_Test(unittest.TestCase):

    def setUp(self):
        self.pfind = partial(
            find_strings, basedir=self._basedir, reducers=[list])

    # Public

    def test_find(self):
        strings = self.pfind(
            string=re.compile('string\d'))
        self.assertEqual(strings, ['string1', 'string2', 'string3'])

    def test_find_with_filename(self):
        strings = self.pfind(
            {'filename': 'file1'},
            string=re.compile('string\d'))
        self.assertEqual(strings, ['string1', 'string3'])

    def test_find_with_filename_and_maxdepth(self):
        strings = self.pfind(
            {'filename': 'file1'}, {'maxdepth': 1},
            string=re.compile('string\d'))
        self.assertEqual(strings, ['string1'])

    # Protected

    @property
    def _basedir(self):
        return os.path.join(os.path.dirname(__file__), 'fixtures')
