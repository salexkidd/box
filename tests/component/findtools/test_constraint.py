import unittest
from box.findtools.constraint import PatternConstraint

class PatternConstraintTest(unittest.TestCase):

    #Public
    
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
    
    #Protected
    
    def _make_mock_constraint_class(self):
        class MockConstraint(PatternConstraint):
            #Protected
            def _match(self, pattern, emitter):
                pass
        return MockConstraint
                