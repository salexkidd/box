import unittest
from box.functools.decorator import Decorator

class DecoratorTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.simple = self._make_mock_simple()
        self.composite = self._make_mock_composite()
        self.Client = self._make_client_class(self.simple, self.composite)
        self.client = self.Client()

    def test_simple(self):
        self.assertEqual(self.client.method1(), 'method')

    def test_composite(self):
        self.assertEqual(self.client.method2(), 'param')

    def test_isinstance(self):
        self.assertIsInstance(self.simple, Decorator)
        self.assertIsInstance(self.simple, type(Decorator))
        # Python doesn't call __instancecheck__ on most of isinstance
        # calls but we have to test instance check inheritance
        self.assertFalse(self.simple.__instancecheck__(Exception))

    # Protected

    def _make_mock_simple(self):
        class simple(Decorator):
            # Public
            def __call__(self, method):
                return method
        return simple

    def _make_mock_composite(self):
        class composite(Decorator):
            # Public
            def __init__(self, param):
                self._param = param
            def __call__(self, method):
                method.param = self._param
                return method
        return composite

    def _make_client_class(self, simple, composite):
        class Client:
            # Public
            @simple
            def method1(self):
                return 'method'
            @composite('param')
            def method2(self):
                return self.method2.param
        return Client
