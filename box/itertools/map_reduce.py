from operator import and_
from functools import reduce

class MapReduce:
    """MapReduce function-class"""
    
    def __call__(self, iterable, mappers=[], reducers=[]):
        values = self._map(iterable, mappers)
        reduced_values = self._reduce(values, reducers)
        return reduced_values

    #Protected
    
    def _map(self, iterable, mappers):
        for emitter in iterable:
            if not isinstance(emitter, MapEmmiter):
                emitter = MapEmmiter(emitter)
            for mapper in mappers:
                mapper(emitter)
            if emitter.skipped:
                continue
            if emitter.emitted:
                yield from emitter.emitted
            else:
                yield emitter.get_value()
            if emitter.stopped:
                break
    
    def _reduce(self, values, reducers):
        result = values
        for reducer in reducers:
            result = reducer(result)
        return result
    

class MapEmmiter:

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
            
    def get_value(self):
        return self._value               
    
    def set_value(self, value, *conditions):
        if reduce(and_, conditions, True):
            self._value = value
        return self
                
    def emit(self, value, *conditions):
        if reduce(and_, conditions, True):
            self._emitted.append(value)
        return self
            
    def skip(self, *conditions):
        if reduce(and_, conditions, True):
            self._skipped = True
        return self
           
    def stop(self, *conditions):
        if reduce(and_, conditions, True):
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


map_reduce = MapReduce()