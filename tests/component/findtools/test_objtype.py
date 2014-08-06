import unittest
from unittest.mock import Mock
from box.findtools.objtype import ObjtypeConstraint


class ObjtypeConstraintTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.emitter = Mock(object=ZeroDivisionError())

    def test___call__(self):
        constraint = ObjtypeConstraint(ArithmeticError)
        constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)

    def test___call___skip(self):
        constraint = ObjtypeConstraint(AssertionError)
        constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)

    def test___call___with_objtype_is_list(self):
        constraint = ObjtypeConstraint([ArithmeticError, BufferError])
        constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)

    def test___call___with_objtype_is_list_skip(self):
        constraint = ObjtypeConstraint([AssertionError, AttributeError])
        constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)
