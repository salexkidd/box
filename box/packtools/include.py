from ..decorator import Decorator

class include(Decorator):

    #Public
    
    attribute_name = '_box_packtools_include'

    def __call__(self, function):
        setattr(function, self.attribute_name, True)
        return function