from abc import ABCMeta, abstractmethod

class Function(ABCMeta):
    """Metaclass making normal class acting like a function.
    """
    
    #Public
    
    def __call__(self, *args, **kwargs):
        function = object.__new__(self)
        function.__init__(*args, **kwargs)
        result = function.__call__()
        return result


class FunctionCall(metaclass=Function):
    """Abstract function call class.
    
    Designed for complicated functions when more convenient to work with state.
    
    On __init__ step your class gets arguments and can save they as attributes. 
    Then on __call__ step your class returns result of function call. 
    
    Inherit from this class to make your class acting like a function::
    
      >>> from box.functools import FunctionCall
      >>> class hello(FunctionCall):
      ...   def __init__(self, person):
      ...     self._person = person
      ...   def __call__(self):
      ...     print('Hello '+self._person+'!')
      >>> hello('World')
      'Hello World!'
    """

    #Public
    
    @abstractmethod    
    def __call__(self):
        pass #pragma: no cover