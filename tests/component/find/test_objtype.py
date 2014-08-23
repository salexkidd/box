import unittest
from unittest.mock import Mock
from box.find.objtype import ObjtypeConstraint


class ObjtypeConstraintTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.constraint = ObjtypeConstraint()
        self.emitter = Mock(objself=ZeroDivisionError())

    def test___call___with_objtype(self):
        self.constraint.extend('objtype', ArithmeticError)
        self.constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)

    def test___call___with_objtype_skip(self):
        self.constraint.extend('objtype', AssertionError)
        self.constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)

    def test___call___with_objtype_is_list(self):
        self.constraint.extend('objtype', [ArithmeticError, BufferError])
        self.constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)

    def test___call___with_objtype_is_list_skip(self):
        self.constraint.extend('objtype', [AssertionError, AttributeError])
        self.constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)

    def test___call___with_notobjtype(self):
        self.constraint.extend('notobjtype', AssertionError)
        self.constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)

    def test___call___with_notobjtype_skip(self):
        self.constraint.extend('notobjtype', ArithmeticError)
        self.constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)