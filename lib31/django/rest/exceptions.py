class RESTException(Exception):
    
    #Public
    
    def __init__(self, value):
        self.__value = value
        
    def __str__(self):
        return self.message

    @property
    def message(self):
        return self.__class__.__name__
    
 
class VersionIsNotSuppported(RESTException): pass
class FormatIsNotSuppported(RESTException): pass
class ResourceIsNotSuppported(RESTException): pass
class ConstraintsAreNotSuppported(RESTException): pass