from ..functools import FunctionCall,  DEFAULT

class map_reduce(FunctionCall):
    
    default_emitter = 'box.itertools.MapEmitter'
    
    def __init__(self, iterable, *, 
                 mappers=[], reducers=[], 
                 emitter=None):
        self._iterable = iterable
        self._mappers = mappers
        self._reducers = reducers
        self._emitter = emitter
        if not self._emitter:
            self._emitter = self.default_emitter
    
    def __call__(self):
        values = self._map()
        reduced_values = self._reduce(values)
        return reduced_values

    #Protected
    
    def _map(self):
        for emitter in self._iterable:
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
        result = values
        for reducer in self._reducers:
            result = reducer(result)
        return result
    
    
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