from ..functools import Function
from .emitter import Emitter
from .not_emitted import NotEmitted


class map_reduce(Function):
    """Process iterable values using map_resuce framework.

    :param iterable values: values to process
    :param list mappers: list of mappers
    :param list reducers: list of reducers
    :param type emitter: emitter class
    :param bool getfirst: return first if True
    :param mixed fallback: fallback if fails

    :returns mixed: map_reduce result
    """

    default_emitter = Emitter
    default_getfirst_exception = NotEmitted

    def __init__(self, values=None, *,
                 mappers=[], reducers=[], emitter=None,
                 getfirst=False, getfirst_exception=None, fallback=None):
        if values is None:
            values = []
        if emitter is None:
            emitter = self.default_emitter
        if getfirst_exception is None:
            getfirst_exception = self.default_getfirst_exception
        self._values = values
        self._mappers = mappers
        self._reducers = reducers
        self._emitter = emitter
        self._getfirst = getfirst
        self._getfirst_exception = getfirst_exception
        self._fallback = fallback

    def __call__(self):
        mapped_values = self._map(self._values)
        reduced_values = self._reduce(mapped_values)
        return reduced_values

    # Protected

    def _map(self, values):
        for emitter in values:
            if not isinstance(emitter, self._emitter):
                emitter = self._emitter(emitter)
            for mapper in self._mappers:
                mapper(emitter)
                if emitter.skipped:
                    break
            if emitter.skipped:
                if emitter.stopped:
                    break
                continue  # pragma: no cover (coverage bug)
            if emitter.emitted:
                yield from emitter.emitted
            else:
                yield emitter.value()
            if emitter.stopped:
                break

    def _reduce(self, values):
        try:
            result = values
            if self._getfirst:
                try:
                    result = next(result)
                except StopIteration:
                    raise self._getfirst_exception()
            for reducer in self._reducers:
                result = reducer(result)
            return result
        except Exception as exception:
            if isinstance(self._fallback, Exception):
                raise self._fallback
            elif callable(self._fallback):
                return self._fallback(exception)
            elif self._fallback is not None:
                return self._fallback
            else:
                raise
