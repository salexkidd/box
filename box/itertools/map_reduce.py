from itertools import chain
from ..functools import Function
from .emitter import Emitter
from .getfirst import GetfirstMapper, GetfirstReducer

class map_reduce(Function):
    """Process iterable values using map_resuce framework.
    
    :param iterable values: values to process
    :param list mappers: list of mappers
    :param list reducers: list of reducers
    :param type emitter: emitter class
    :param bool getfirst: return first if True
    :param mixed fallback: fallback if fails
    
    :returns mixed: map_reduce result
    """
    
    default_emitter = Emitter
    
    def __init__(self, values=[], *, 
                 mappers=[], reducers=[], emitter=None, 
                 getfirst=False, fallback=None):
        self._user_values = values
        self._user_mappers = mappers
        self._user_reducers = reducers
        self._emitter = emitter
        self._getfirst = getfirst        
        self._fallback = fallback
        if not self._emitter:
            self._emitter = self.default_emitter
    
    def __call__(self):
        mapped_values = self._map(self._values)
        reduced_values = self._reduce(mapped_values)
        return reduced_values

    #Protected

    _extension_values = []
    _extension_mappers = []
    _extension_reducers = []
    _getfirst_exception = None
    
    def _map(self, values):
        for emitter in values:
            if not isinstance(emitter, self._emitter):
                emitter = self._emitter(emitter)
            for mapper in self._mappers:
                mapper(emitter)
                if emitter.skipped:
                    break
            if emitter.skipped:
                if emitter.stopped:
                    break
                continue #pragma: no cover (coverage bug)
            if emitter.emitted:
                yield from emitter.emitted
            else:
                yield emitter.value()
            if emitter.stopped:
                break
    
    def _reduce(self, values):
        try:
            result = values
            for reducer in self._reducers:
                result = reducer(result)
            return result
        except Exception as exception:
            if isinstance(self._fallback, Exception):
                raise self._fallback
            elif callable(self._fallback):
                return self._fallback(exception)            
            elif self._fallback != None:
                return self._fallback
            else:
                raise
            
    @property            
    def _values(self):
        return chain(
            self._system_values,
            self._extension_values,
            self._user_values)
    
    @property        
    def _mappers(self):
        return chain(
            self._system_mappers,                
            self._extension_mappers,
            self._user_mappers)    
    
    @property        
    def _reducers(self):
        return chain(
            self._system_reducers,
            self._extension_reducers,
            self._user_reducers)
    
    @property
    def _system_values(self):
        return []
        
    @property
    def _system_mappers(self):
        return [GetfirstMapper(
            self._getfirst)]
    
    @property
    def _system_reducers(self):
        return [GetfirstReducer(
            self._getfirst, 
            self._getfirst_exception)]