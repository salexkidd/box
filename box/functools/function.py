from abc import ABCMeta, abstractmethod


class FunctionMetaclass(ABCMeta):
    """Metaclass making normal class acting like a function.
    """

    # Public

    def __call__(self, *args, **kwargs):
        function = object.__new__(self)
        function.__init__(*args, **kwargs)
        result = function.__call__()
        return result

    def __instancecheck__(self, instance):
        result = issubclass(instance, self)
        if not result:
            result = super().__instancecheck__(instance)
        return result


class Function(metaclass=FunctionMetaclass):
    """Base abstract class for 2 step functions.

    Designed for complicated functions when more convenient to work with state.

    On __init__ step your class gets arguments and can save they as attributes.
    Then on __call__ step your class returns result of function call.

    Inherit from this class to make your class acting like a function::

      >>> from box.functools import Function
      >>> class hello(Function):
      ...   def __init__(self, person):
      ...     self._person = person
      ...   def __call__(self):
      ...     print('Hello '+self._person+'!')
      >>> hello('World')
      'Hello World!'
    """

    # Public

    @abstractmethod
    def __call__(self):
        """Abstract method to implement.
        """
        pass  # pragma: no cover
