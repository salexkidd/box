import re
import unittest
from unittest.mock import Mock
from box.find.objname import ObjnameConstraint


class ObjnameConstraintTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.constraint = ObjnameConstraint()
        self.emitter = Mock(objname='objname')

    def test___call___with_objname(self):
        self.constraint.extend('objname', 'objname')
        self.constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)

    def test___call___with_objname_skip(self):
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

    def test___call___with_notobjname(self):
        self.constraint.extend('notobjname', 'x')
        self.constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)

    def test___call___with_notobjname_skip(self):
        self.constraint.extend('notobjname', 'objname')
        self.constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)
