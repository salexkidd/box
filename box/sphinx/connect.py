import functools
from ..functools import Decorator


class connect(Decorator):
    """Decorate method to be connected to sphinx event.

    Parameters
    ----------
    event: str
        Sphinx event.
    """

    # Public

    marker = '_box_sphinx_connect'

    def __init__(self, event):
        self.__event = event

    def __call__(self, method):
        self.__method = method
        setattr(method, self.marker, self)
        return method

    def invoke(self, obj, app):
        app.connect(self.__event, functools.partial(self.__method, obj))
