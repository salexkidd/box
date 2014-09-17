import unittest
from unittest.mock import Mock
from importlib import import_module
component = import_module('box.importlib.inject')


class inject_Test(unittest.TestCase):

    # Actions

    def setUp(self):
        self.Client = self.make_client_class()
        self.client = self.Client()

    # Helpers

    def make_client_class(self):
        class Client:
            # Public
            injection = component.inject('unittest.mock.Mock')
        return Client

    # Tests

    def test(self):
        self.assertEqual(self.client.injection, Mock)
