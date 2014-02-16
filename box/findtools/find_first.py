from itertools import chain
from .not_found import NotFound

class FindFirstMixin:

    #Protected
    
    @property
    def _builtin_mappers(self):
        return chain(super()._builtin_mappers, [FindFirstMapper()])
    
    @property
    def _builtin_reducers(self):
        return chain(super()._builtin_reducers, [FindFirstReducer()])
 
 
class FindFirstMapper:

    #Public

    def __call__(self, emitter):
        if not emitter.skipped:
            emitter.stop()
    
    
class FindFirstReducer:

    #Public

    def __call__(self, values):
        if len(values) >= 1:
            return values[0]
        else:
            raise NotFound()