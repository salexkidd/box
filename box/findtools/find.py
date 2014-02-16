from abc import ABCMeta, abstractmethod
from ..functools import FunctionCall
from ..itertools import map_reduce

class find(FunctionCall, metaclass=ABCMeta):

    #Public          
            
    def __call__(self):
        result = map_reduce(
            self._iterable, 
            mappers=self._effective_mappers, 
            reducers=self._effective_reducers,
            fallback=self._fallback)
        return result
            
    #Protected
           
    _builtin_mappers = []
    _builtin_reducers = []
    _fallback = None
    
    @property
    @abstractmethod
    def _iterable(self):
        pass #pragma: no cover 
    
    @property        
    def _effective_mappers(self):
        return self._builtin_mappers+self._mappers    
    
    @property        
    def _effective_reducers(self):
        return self._builtin_reducers+self._reducers