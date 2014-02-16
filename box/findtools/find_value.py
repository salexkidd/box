from itertools import chain
from .not_found import NotFound

class FindValueMixin:

    #Protected
    
    @property
    def _builtin_mappers(self):
        return chain(super()._builtin_mappers, [FindValueMapper()])
    
    @property
    def _builtin_reducers(self):
        return chain(super()._builtin_reducers, [FindValueReducer()])
 
 
class FindValueMapper:

    #Public

    def __call__(self, emitter):
        if not emitter.skipped:
            emitter.stop()
    
    
class FindValueReducer:

    #Public

    def __call__(self, values):
        if len(values) >= 1:
            return values[0]
        else:
            raise NotFound()