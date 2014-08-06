import os
import unittest
from unittest.mock import Mock
from box.findtools.maxdepth import MaxdepthConstraint


class MaxdepthConstraintTest(unittest.TestCase):

    # Public

    def setUp(self):
        # Depth is 2
        self.emitter = Mock(filepath=os.path.join('file', 'path'))

    def test___call__(self):
        constraint = MaxdepthConstraint(2)
        constraint(self.emitter)
        self.assertFalse(self.emitter.skip.called)
        self.assertFalse(self.emitter.stop.called)

    def test___call___skip(self):
        constraint = MaxdepthConstraint(1)
        constraint(self.emitter)
        self.assertTrue(self.emitter.skip.called)
        self.assertTrue(self.emitter.stop.called)
