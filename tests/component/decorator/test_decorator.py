import unittest
from box.decorator.decorator import Decorator

class DecoratorTest(unittest.TestCase):

    #Public

    def test(self):
        decorator = self._make_mock_decorator()
        self.assertEqual(decorator('method'), 'method')

    def test_with_init(self):
        decorator = self._make_mock_decorator_with_init()
        self.assertEqual(decorator('param')('method'), ('param', 'method'))        
    
    #Protected
    
    def _make_mock_decorator(self):
        class decorator(Decorator):
            #Public
            def __call__(self, method):
                return method
        return decorator
            
    def _make_mock_decorator_with_init(self):
        class decorator(Decorator):
            #Public
            def __init__(self, param):
                self._param = param
            def __call__(self, method):
                return (self._param, method)                
        return decorator                     