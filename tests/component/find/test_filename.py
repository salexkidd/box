import re
import unittest
from unittest.mock import Mock
from box.find.filename import FilenameConstraint


class FilenameConstraintTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.constraint = FilenameConstraint()
        self.emitter = Mock(filename='filename')

    def test___call__(self):
        self.constraint.extend('filename', 'f*')
        self.constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)

    def test___call___skip(self):
        self.constraint.extend('filename', 'x*')
        self.constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)

    def test___call___with_filename_is_regex(self):
        self.constraint.extend('filename', re.compile('f.*'))
        self.constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)

    def test___call___with_filename_is_regex_skip(self):
        self.constraint.extend('filename', re.compile('x.*'))
        self.constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)
