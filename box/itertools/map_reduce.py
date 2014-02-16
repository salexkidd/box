from itertools import chain
from ..functools import FunctionCall,  DEFAULT

class map_reduce(FunctionCall):
    
    default_emitter = 'deferred:MapEmitter'
    
    def __init__(self, values=[], *args, 
                 mappers=[], reducers=[], 
                 emitter=None, fallback=None, **kwargs):
        self._user_values = values
        self._user_mappers = mappers
        self._user_reducers = reducers
        self._emitter = emitter
        self._fallback = fallback
        if not self._emitter:
            self._emitter = self.default_emitter
    
    def __call__(self):
        mapped_values = self._map(self._values)
        reduced_values = self._reduce(mapped_values)
        return reduced_values

    #Protected
    
    _builtin_values = []
    _builtin_mappers = []
    _builtin_reducers = []
    
    def _map(self, values):
        for emitter in values:
            if not isinstance(emitter, self._emitter):
                emitter = self._emitter(emitter)
            for mapper in self._mappers:
                mapper(emitter)
                if emitter.skipped:
                    break
            if emitter.skipped:
                continue
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
        return chain(self._builtin_values, 
                     self._user_values)
    
    @property        
    def _mappers(self):
        return chain(self._builtin_mappers, 
                     self._user_mappers)    
    
    @property        
    def _reducers(self):
        return chain(self._builtin_reducers, 
                     self._user_reducers)
    
    
class MapEmitter:

    #Public

    def __init__(self, value, **context):
        self._value = value
        self._context = context
        self._emitted = []
        self._skipped = False
        self._stopped = False
            
    def __getattr__(self, name):
        try:
            return self._context[name]
        except KeyError:
            raise AttributeError(name)
    
    def value(self, value=DEFAULT, condition=None):
        if value == DEFAULT:
            return self._value
        else:
            if condition == None or condition:
                self._value = value
            return self
                
    def emit(self, value, condition=None):
        if condition == None or condition:
            self._emitted.append(value)
        return self
            
    def skip(self, condition=None):
        if condition == None or condition:
            self._skipped = True
        return self
           
    def stop(self, condition=None):
        if condition == None or condition:
            self._stopped = True
        return self
    
    @property
    def emitted(self):
        return self._emitted
    
    @property
    def skipped(self):
        return self._skipped
    
    @property
    def stopped(self):
        return self._stopped  
    
    
map_reduce.default_emitter = MapEmitter  