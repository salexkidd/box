import inspect
from abc import ABCMeta, abstractmethod


class Metaclass(ABCMeta):
    """Metaclass to unify simple and composite decorators implimentation.
    """

    # Public

    def __call__(self, *args, **kwargs):
        decorator = object.__new__(self)
        if decorator.is_composite(*args, **kwargs):
            # Composite decorator
            decorator.__init__(*args, **kwargs)
            return decorator
        else:
            # Simple decorator
            decorator.__init__()
            result = decorator.__call__(args[0])
            return result

    def __instancecheck__(self, instance):
        result = issubclass(instance, self)
        if not result:
            result = super().__instancecheck__(instance)
        return result


class Decorator(metaclass=Metaclass):
    """Base abstract class for unified simple and composite decorators.

    Examples
    --------
    With default is_composite implementation it checks if first positional
    argument is function or not and acts correspondingly::

        class decorator(Decorator):
            def __init__(self, param=None):
                self.__param = param
            def __call__(self, function):
                return function

        @decorator
        def function(self):
            pass

        @decorator('param')
        def function(self):
            pass
    """

    # Public

    @abstractmethod
    def __call__(self, function):
        """Abstract method to implement.
        """
        pass  # pragma: no cover

    def is_composite(self, *args, **kwargs):
        """Define decorator is composite for the given arguments.
        """
        try:
            return not inspect.isfunction(args[0])
        except KeyError:
            return False
