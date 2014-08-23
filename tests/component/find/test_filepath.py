import re
import unittest
from unittest.mock import Mock
from box.find.filepath import FilepathConstraint


class FilepathConstraintTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.constraint = FilepathConstraint()
        self.emitter = Mock(filepath='filepath')

    def test___call___with_filepath(self):
        self.constraint.extend('filepath', 'f*')
        self.constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)

    def test___call___with_filepath_skip(self):
        self.constraint.extend('filepath', 'x*')
        self.constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)

    def test___call___with_filepath_is_regex(self):
        self.constraint.extend('filepath', re.compile('f.*'))
        self.constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)

    def test___call___with_filepath_is_regex_skip(self):
        self.constraint.extend('filepath', re.compile('x.*'))
        self.constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)

    def test___call___with_notfilepath(self):
        self.constraint.extend('notfilepath', 'x*')
        self.constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)

    def test___call___with_notfilepathh_skip(self):
        self.constraint.extend('notfilepath', 'f*')
        self.constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)
