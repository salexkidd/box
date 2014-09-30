import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('box.sphinx.setup')


class setup_Test(unittest.TestCase):

    # Actions

    def setUp(self):
        self.method = Mock()
        self.method = component.setup(self.method)

    # Helpers

    def test(self):
        setup = getattr(self.method, component.setup.decorator)
        setup.invoke('obj', 'app')
        self.method.assert_called_with('obj', 'app')
