from ..functools import FunctionCall
from .map_emitter import MapEmmiter

class map_reduce(FunctionCall):
    
    default_emitter = MapEmmiter
    
    def __init__(self, iterable, *, 
                 mappers=[], reducers=[], emitter=None):
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