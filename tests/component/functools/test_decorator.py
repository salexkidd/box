import unittest
from importlib import import_module
component = import_module('box.functools.decorator')


class DecoratorTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.simple = self.make_mock_simple()
        self.composite = self.make_mock_composite()
        self.Client = self.make_client_class(self.simple, self.composite)
        self.client = self.Client()

    # Helpers

    def make_mock_simple(self):
        class simple(component.Decorator):
            # Public
            def __call__(self, method):
                return method
        return simple

    def make_mock_composite(self):
        class composite(component.Decorator):
            # Public
            def __init__(self, param):
                self._param = param
            def __call__(self, method):
                method.param = self._param
                return method
        return composite

    def make_client_class(self, simple, composite):
        class Client:
            # Public
            @simple
            def method1(self):
                return 'method'
            @composite('param')
            def method2(self):
                return self.method2.param
        return Client

    # Tests

    def test_simple(self):
        self.assertEqual(self.client.method1(), 'method')

    def test_composite(self):
        self.assertEqual(self.client.method2(), 'param')

    def test_isinstance(self):
        self.assertIsInstance(self.simple, component.Decorator)
        self.assertIsInstance(self.simple, type(component.Decorator))
        # Python doesn't call __instancecheck__ on most of isinstance
        # calls but we have to test instance check inheritance
        self.assertFalse(self.simple.__instancecheck__(Exception))
