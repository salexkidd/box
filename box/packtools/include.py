from ..decorator import Decorator

class include(Decorator):
    """Decorate callable object to be included in settings.
    """

    #Public
    
    attribute_name = '_box_packtools_include'

    def __call__(self, obj):
        setattr(obj, self.attribute_name, True)
        return obj