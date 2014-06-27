from abc import ABCMeta, abstractmethod

class Condition(metaclass=ABCMeta):

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
    
    def match(self, value):
        if self._include != None:
            if self._effective_match(self._include, value):
                return True
        if self._exclude:
            if not self._effective_match(self._exclude, value):
                return True
        return False
    
    #Protected
    
    @abstractmethod
    def _effective_match(self, pattern, value):
        pass #pragma: no cover