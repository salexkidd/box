import re
import unittest
from unittest.mock import Mock
from box.findtools.filename import FilenameConstraint


class FilenameConstraintTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.emitter = Mock(filename='filename')

    def test___call__(self):
        constraint = FilenameConstraint('f*')
        constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)

    def test___call___skip(self):
        constraint = FilenameConstraint('x*')
        constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)

    def test___call___with_filename_is_regex(self):
        constraint = FilenameConstraint(re.compile('f.*'))
        constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)

    def test___call___with_filename_is_regex_skip(self):
        constraint = FilenameConstraint(re.compile('x.*'))
        constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)
