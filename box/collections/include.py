from ..functools import Decorator


class include(Decorator):
    """Decorate callable object to be included to settings.
    """

    # Public

    marker = '_box_collections_include'

    def __call__(self, method):
        setattr(method, self.marker, True)
        return method
