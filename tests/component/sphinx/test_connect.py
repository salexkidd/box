import unittest
from unittest.mock import Mock, patch
from importlib import import_module
component = import_module('box.sphinx.connect')


class connect_Test(unittest.TestCase):

    # Actions

    def setUp(self):
        self.method = Mock()
        self.method = component.connect('event')(self.method)

    # Tests

    @patch.object(component.functools, 'partial')
    def test(self, partial):
        app = Mock()
        connect = getattr(self.method, component.connect.decorator)
        connect.invoke('obj', app)
        app.connect.assert_called_with('event', partial.return_value)
        partial.assert_called_with(self.method, 'obj')
