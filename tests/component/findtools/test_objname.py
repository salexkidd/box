import re
import unittest
from unittest.mock import Mock
from box.findtools.objname import ObjnameConstraint


class ObjnameConstraintTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.constraint = ObjnameConstraint()
        self.emitter = Mock(objname='objname')

    def test___call__(self):
        self.constraint.extend('objname', 'objname')
        self.constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)

    def test___call___skip(self):
        self.constraint.extend('objname', 'x')
        self.constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)

    def test___call___with_objname_is_regex(self):
        self.constraint.extend('objname', re.compile('o.*'))
        self.constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)

    def test___call___with_objname_is_regex_skip(self):
        self.constraint.extend('objname', re.compile('x.*'))
        self.constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)
