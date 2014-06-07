from .not_emitted import NotEmitted

class GetfirstMapper:

    #Public
    
    def __init__(self, getfirst):
        self._getfirst = getfirst

    def __call__(self, emitter):
        if self._getfirst:
            emitter.stop(if_not_skipped=True)
            

class GetfirstReducer:

    #Public
    
    default_exception = NotEmitted
    
    def __init__(self, getfirst, exception=None):
        self._getfirst = getfirst        
        self._exception = exception
        if self._exception == None:
            self._exception = self.default_exception

    def __call__(self, values):
        if self._getfirst:
            try:
                return next(values)
            except Exception:
                raise self._exception()
        else:
            return values            