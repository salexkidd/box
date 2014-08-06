import unittest
from unittest.mock import Mock
from box.sphinx.setup import setup as sphinx_setup


class setup_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.method = Mock()
        self.method = sphinx_setup(self.method)

    def test(self):
        setup = getattr(self.method, sphinx_setup.attribute_name)
        setup.invoke('obj', 'app')
        self.method.assert_called_with('obj', 'app')
