from ..decorator import Decorator

class include(Decorator):
    """Decorate function/method to be included in settings.
    """

    #Public
    
    attribute_name = '_box_packtools_include'

    def __call__(self, function):
        setattr(function, self.attribute_name, True)
        return function