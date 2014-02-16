from abc import ABCMeta, abstractmethod
from ..functools import FunctionCall
from .map_reduce import map_reduce

class MapReduceCall(FunctionCall, metaclass=ABCMeta):

    #Public
            
    def __call__(self):
        result = map_reduce(
            self._iterable, 
            mappers=self._mappers, 
            reducers=self._reducers,
            emitter=self._emitter,
            fallback=self._fallback)
        return result
            
    #Protected
           
    _builtin_mappers = []
    _builtin_reducers = []
    _user_mappers = []
    _user_reducers = []
    _emitter = None
    _fallback = None
    
    @property
    @abstractmethod
    def _iterable(self):
        pass #pragma: no cover 
    
    @property        
    def _mappers(self):
        return self._builtin_mappers+self._user_mappers    
    
    @property        
    def _reducers(self):
        return self._builtin_reducers+self._user_reducers