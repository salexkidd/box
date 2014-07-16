from ..functools import DEFAULT

class Emitter:
    """Emitter representation for map_reduce.
    
    :param mixed value: initial value to emit
    :param dict context: items will be available as emitter's attributes
    """

    # Public

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
        """Get/set value to emit.
        
        :param mixed value: value to set if passed
        :param bool condition: set only if condition is True
        
        Use emitter.value(value) to emit only one value.
        """
        if value == DEFAULT:
            return self._value
        else:
            if condition:
                self._value = value
            return self

    def emit(self, value, condition=True):
        """Emit value.
        
        :param mixed value: value to emit
        :param bool condition: emit only if condition is True
        
        If you need emit more than one emitter.value() you may use
        emitter.emit(value) many times. All values will be emitted
        but **emitter.value() will be ignored**.
        """
        if condition:
            self._emitted.append(value)
        return self

    def skip(self, condition=True):
        """Skip iteration.
        
        :param bool condition: skip only if condition is True
        
        Nothing will be emitted in this iteration.
        """
        if condition:
            self._skipped = True
        return self

    def stop(self, condition=True, *, if_not_skipped=False):
        """Stop iteration.
        
        :param bool condition: stop only if condition is True
        :param bool if_not_skipped: stop only if not skipped
        
        Map cycle will be stopped on this iteration.
        """
        if condition:
            if if_not_skipped:
                self._stopped_if_not_skipped = True
            else:
                self._stopped = True
        return self

    @property
    def emitted(self):
        """Emitted values.
        """
        return self._emitted

    @property
    def skipped(self):
        """Skipped flag.
        """
        return self._skipped

    @property
    def stopped(self):
        """Stopped flag.
        """
        if self._stopped:
            return self._stopped
        else:
            if self._stopped_if_not_skipped:
                return not self._skipped
            else:
                return False
