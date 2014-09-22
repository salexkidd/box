from ..functools import Decorator


class include(Decorator):
    """Decorate callable object to be included to settings.
    """

    # Public

    attribute_name = '_box_collections_include'

    def __call__(self, method):
        setattr(method, self.attribute_name, True)
        return method
