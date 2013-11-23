class RestException(Exception):
    
    #Public
    
    def __init__(self, value):
        self.__value = value
        
    def __str__(self):
        return self.message

    @property
    def message(self):
        return self.__class__.__name__
    
 
class VersionIsNotSuppported(RestException): pass
class FormatIsNotSuppported(RestException): pass
class ResourceIsNotSuppported(RestException): pass
class ConstraintsAreNotSuppported(RestException):pass