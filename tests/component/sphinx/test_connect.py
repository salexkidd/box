import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('box.sphinx.connect')


class connect_Test(unittest.TestCase):

    # Actions

    def setUp(self):
        self.method = Mock()
        self.method = component.connect('event')(self.method)

    # Tests

    def test(self):
        app = Mock()
        connect = getattr(self.method, component.connect.decorator)
        connect.invoke('function', app)
        app.connect.assert_called_with('event', 'function')
