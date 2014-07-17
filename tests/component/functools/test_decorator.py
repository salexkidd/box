import unittest
from box.functools.decorator import Decorator

class DecoratorTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.decorator1 = self._make_mock_decorator1()
        self.decorator2 = self._make_mock_decorator2()
        self.client_class = self._make_client_class(
            self.decorator1, self.decorator2)
        self.client = self.client_class()

    def test_1_step(self):
        self.assertEqual(self.client.method1(), 'method')

    def test_2_steps(self):
        self.assertEqual(self.client.method2(), 'param')

    def test_isinstance(self):
        self.assertIsInstance(self.decorator1, Decorator)
        self.assertIsInstance(self.decorator1, type(Decorator))
        # Python doesn't call __instancecheck__ on most of isinstance
        # calls but we have to test instance check inheritance
        self.assertFalse(self.decorator1.__instancecheck__(Exception))

    # Protected

    def _make_mock_decorator1(self):
        class decorator1(Decorator):
            # Public
            def __call__(self, method):
                return method
        return decorator1

    def _make_mock_decorator2(self):
        class decorator2(Decorator):
            # Public
            def __init__(self, param):
                self._param = param
            def __call__(self, method):
                method.param = self._param
                return method
        return decorator2

    def _make_client_class(self, decorator1, decorator2):
        class Client:
            # Public
            @decorator1
            def method1(self):
                return 'method'
            @decorator2('param')
            def method2(self):
                return self.method2.param
        return Client
