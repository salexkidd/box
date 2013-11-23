class APIException(Exception):
    
    #Public
    
    def __init__(self, value):
        self.__value = value
        
    def __str__(self):
        return self.message

    @property
    def message(self):
        return self.__class__.__name__
    
 
class VersionIsNotSuppported(APIException): pass
class FormatIsNotSuppported(APIException): pass
class ResourceIsNotSuppported(APIException): pass
class ConstraintsAreNotSuppported(APIException):pass