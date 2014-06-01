from ..functools import DEFAULT

class Emitter:

    #Public

    def __init__(self, value, **context):
        self._value = value
        self._context = context
        self._emitted = []
        self._skipped = False
        self._stopped = False
        self._stopped_if_not_skipped = False
            
    def __getattr__(self, name):
        try:
            return self._context[name]
        except KeyError:
            raise AttributeError(name)
    
    def value(self, value=DEFAULT, condition=True):
        if value == DEFAULT:
            return self._value
        else:
            if condition:
                self._value = value
            return self
                
    def emit(self, value, condition=True):
        if condition:
            self._emitted.append(value)
        return self
            
    def skip(self, condition=True):
        if condition:
            self._skipped = True
        return self
           
    def stop(self, condition=True, *, if_not_skipped=False):
        if condition:
            if if_not_skipped:
                self._stopped_if_not_skipped = True
            else:
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
        if self._stopped:
            return self._stopped
        else:
            if self._stopped_if_not_skipped:
                return not self._skipped
            else:
                return False