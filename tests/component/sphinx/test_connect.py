import unittest
from unittest.mock import Mock, patch
from box.sphinx.connect import functools, connect as sphinx_connect

class connect_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.method = Mock()
        self.method = sphinx_connect('event')(self.method)
     
    @patch.object(functools, 'partial')   
    def test(self, partial):
        app = Mock()
        connect = getattr(self.method, sphinx_connect.attribute_name)
        connect.invoke('obj', app)
        app.connect.assert_called_with('event', partial.return_value)
        partial.assert_called_with(self.method, 'obj')