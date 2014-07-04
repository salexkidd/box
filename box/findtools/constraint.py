from abc import ABCMeta, abstractmethod

class Constraint(metaclass=ABCMeta):

    #Public

    @abstractmethod
    def __call__(self, emitter):
        pass #pragma: no cover
    
    
class CompositeConstraint(Constraint, metaclass=ABCMeta):
    
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
    
    
class PatternConstraint(CompositeConstraint, metaclass=ABCMeta):
    
    #Publilc
    
    def __call__(self, emitter):
        if self._include != None:
            if not self._match(self._include, emitter):
                emitter.skip()
        if self._exclude:
            if self._match(self._exclude, emitter):
                emitter.skip()
        
    #Protected    
        
    @abstractmethod
    def _match(self, pattern, emitter):
        pass #pragma: no cover    