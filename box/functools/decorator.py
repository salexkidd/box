from abc import ABCMeta, abstractmethod


class Metaclass(ABCMeta):
    """Metaclass to unify simple and composite decorators implimentation.
    """

    # Public

    def __call__(self, *args, **kwargs):
        decorator = object.__new__(self)
        if decorator._is_composite(*args, **kwargs):
            # Composite decorator
            decorator.__init__(*args, **kwargs)
            return decorator
        else:
            # Simple decorator
            result = decorator.__call__(*args, **kwargs)
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
    Let see the difference between simple and composite decorators:

    - By default if Decorator implementation doesn't override __init__ method
      it works as simple decorator without arguments::

        class decorator(Decorator):
            def __call__(self, function):
                return function

        @decorator
        def function(self):
            pass

    - Otherwise it works as composite decorator, accepts arguments
      and calls __init__ with the given arguments::

        class decorator(Decorator):
            def __init__(self, param):
                self._param = param
            def __call__(self, function):
                print(self._param)
                return function

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

    # Protected

    def _is_composite(self, *args, **kwargs):
        """Check decorator is composite for the given arguments.

        Overriding this method you can define type of your decorator.
        """
        return not (getattr(type(self), '__init__') is object.__init__)
