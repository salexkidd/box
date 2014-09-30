from ..functools import Decorator


class setup(Decorator):
    """Decorate method to be added to sphinx setup.
    """

    # Public

    marker = '_box_sphinx_setup'

    def __call__(self, method):
        self.__method = method
        setattr(method, self.marker, self)
        return method

    def invoke(self, obj, app):
        self._method(obj, app)

    # Protected

    @property
    def _method(self):
        return self.__method
