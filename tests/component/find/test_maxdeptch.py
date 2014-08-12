import os
import unittest
from unittest.mock import Mock
from box.find.maxdepth import MaxdepthConstraint


class MaxdepthConstraintTest(unittest.TestCase):

    # Public

    def setUp(self):
        # Depth is 2
        self.emitter = Mock(filepath=os.path.join('file', 'path'))
        self.constraint = MaxdepthConstraint()

    def test___call__(self):
        self.constraint.extend('maxdepth', 2)
        self.constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)
        self.assertFalse(self.emitter.stop.called)

    def test___call___skip(self):
        self.constraint.extend('maxdepth', 1)
        self.constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)
        self.assertTrue(self.emitter.stop.called)
