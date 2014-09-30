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
        self.__method(obj, app)
