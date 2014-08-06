from ..functools import Decorator


class setup(Decorator):
    """Decorate method to be added to sphinx setup.
    """

    # Public

    attribute_name = '_box_sphinx_setup'

    def __call__(self, method):
        self._method = method
        setattr(method, self.attribute_name, self)
        return method

    def invoke(self, obj, app):
        self._method(obj, app)
