from ..types import Null


class Emitter:
    """Emitter representation for map_reduce.

    Parameters
    ----------
    value: mixed
        Initial value to emit.
    context: dict
        Items will be available as emitter's attributes.
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

    def value(self, value=Null, condition=True):
        """Get/set value to emit.

        Use emitter.value(value) to emit only one value.

        Parameters
        ----------
        value: mixed
            Value to set if passed.
        condition: bool
            Set only if condition is True.
        """
        if value is Null:
            return self._value
        else:
            if condition:
                self._value = value
            return self

    def emit(self, value, condition=True):
        """Emit value.

        If you need emit more than one emitter.value() you may use
        emitter.emit(value) many times. All values will be emitted
        but **emitter.value() will be ignored**.

        Parameters
        ----------
        value: mixed
            Value to emit.
        condition: bool
            Emit only if condition is True.
        """
        if condition:
            self._emitted.append(value)
        return self

    def skip(self, condition=True):
        """Skip iteration.

        Nothing will be emitted in this iteration.

        Parameters
        ----------
        condition: bool
            Skip only if condition is True.
        """
        if condition:
            self._skipped = True
        return self

    def stop(self, condition=True, *, if_not_skipped=False):
        """Stop iteration.

        Map cycle will be stopped on this iteration.

        Parameters
        ----------
        condition: bool
            Stop only if condition is True.
        if_not_skipped: bool
            Stop only if not skipped.
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
