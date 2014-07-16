from itertools import chain
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

    def __init__(self, values=[], *,
                 mappers=[], reducers=[], emitter=None,
                 getfirst=False, fallback=None):
        if emitter == None:
            emitter = self.default_emitter
        self._user_values = values
        self._user_mappers = mappers
        self._user_reducers = reducers
        self._emitter = emitter
        self._getfirst = getfirst
        self._fallback = fallback

    def __call__(self):
        mapped_values = self._map(self._values)
        reduced_values = self._reduce(mapped_values)
        return reduced_values

    # Protected

    _system_values = []
    _system_mappers = []
    _system_reducers = []
    _getfirst_exception = NotEmitted

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
            elif self._fallback != None:
                return self._fallback
            else:
                raise

    @property
    def _values(self):
        return chain(
            self._system_values,
            self._user_values)

    @property
    def _mappers(self):
        return chain(
            self._system_mappers,
            self._user_mappers)

    @property
    def _reducers(self):
        return chain(
            self._system_reducers,
            self._user_reducers)
