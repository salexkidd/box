import unittest
from unittest.mock import Mock
from box.findtools.constraint import PatternConstraint

class PatternConstraintTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.Constraint = self._make_mock_constraint_class()
        self.constraint = self.Constraint('include', 'exclude')

    def test___bool__(self):
        self.assertTrue(self.constraint)

    def test___bool___with_empty_constraint(self):
        constraint = self.Constraint()
        self.assertFalse(constraint)

    def test___repr__(self):
        self.assertIn('include', repr(self.constraint))
        self.assertIn('exclude', repr(self.constraint))

    def test___call___not_skip(self):
        emitter = Mock()
        emitter.include = True
        emitter.exclude = False
        self.constraint(emitter)
        self.assertFalse(emitter.skip.called)

    def test___call___skip(self):
        emitter = Mock()
        emitter.include = False
        emitter.exclude = True
        self.constraint(emitter)
        self.assertTrue(emitter.skip.called)

    # Protected

    def _make_mock_constraint_class(self):
        class MockConstraint(PatternConstraint):
            # Protected
            def _match(self, pattern, emitter):
                return getattr(emitter, pattern)
        return MockConstraint
