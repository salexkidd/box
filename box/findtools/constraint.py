from abc import ABCMeta, abstractmethod

class Constraint(metaclass=ABCMeta):

    #Public

    def __init__(self, include=None, exclude=None):
        self._include = include
        self._exclude = exclude
    
    def __bool__(self):
        return (self._include != None or 
                self._exclude != None)
    
    def __repr__(self):
        return ('Include: {include}, exclude: {exclude}'.
                format(include=self._include,
                       exclude=self._exclude))
    
    @abstractmethod
    def check(self, value):
        pass #pragma: no cover
    
    
class PatternConstraint(Constraint, metaclass=ABCMeta):
    
    #Publilc
    
    def check(self, value):
        if self._include != None:
            if self._match(self._include, value):
                return True
        if self._exclude:
            if not self._match(self._exclude, value):
                return True
        return False
    
    #Protected
    
    @abstractmethod
    def _match(self, pattern, value):
        pass #pragma: no cover    