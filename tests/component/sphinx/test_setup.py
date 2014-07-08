import unittest
from unittest.mock import Mock
from box.sphinx.setup import setup as sphinx_setup

class setup_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.method = Mock()
        sphinx_setup(self.method)

    def test(self):
        sphinx_setup