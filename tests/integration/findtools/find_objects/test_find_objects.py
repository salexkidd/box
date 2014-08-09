import os
import re
import unittest
from functools import partial
# TODO: Nose in shell imports module instead of object
from box.findtools.find_objects import find_objects


class find_objects_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.pfind = partial(
            find_objects, basedir=self._basedir, reducers=[list])

    def test_find_with_objname_and_filename(self):
        objects = self.pfind(
            {'objname': re.compile('attr\d')},
            {'filename': 'module1.py'})
        self.assertEqual(objects, ['attr1', 'attr3'])

    def test_find_with_objname_and_filename_and_maxdepth(self):
        objects = self.pfind(
            {'objname': re.compile('attr\d')},
            {'filename': 'module1.py'},
            {'maxdepth': 1})
        self.assertEqual(objects, ['attr1'])

    # Protected

    @property
    def _basedir(self):
        return os.path.join(os.path.dirname(__file__), 'fixtures')
