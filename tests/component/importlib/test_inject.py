import unittest
from unittest.mock import Mock
from box.importlib.inject import inject

class inject_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.Client = self._make_client_class()
        self.client = self.Client()

    def test(self):
        self.assertEqual(self.client.injection, Mock)

    # Protected

    def _make_client_class(self):
        class Client:
            # Public
            injection = inject('unittest.mock.Mock')
        return Client
