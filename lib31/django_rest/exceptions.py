class BadRequest(Exception):
    
    #Public
    
    def __init__(self, value):
        self.__value = value
        
    def __str__(self):
        return self.message

    @property
    def message(self):
        return self.__class__.__name__
    
 
class VersionIsNotSuppported(BadRequest): pass
class FormatIsNotSuppported(BadRequest): pass
class ResourceIsNotSuppported(BadRequest): pass
class ConstraintsAreNotSuppported(BadRequest): pass