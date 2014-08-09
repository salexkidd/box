from abc import ABCMeta, abstractmethod
from ..functools import Function
from ..importlib import inject
from ..itertools import map_reduce, Emitter
from .not_found import NotFound


class find(Function, metaclass=ABCMeta):
    """Find framework base class.
    """

    # Public

    default_emitter = inject('FindEmitter', module=__name__)
    default_getfirst_exception = NotFound

    def __init__(self, *,
                 filters=None, constraints=None,
                 mappers=None, reducers=None, emitter=None,
                 getfirst=False, getfirst_exception=None, fallback=None):
        if filters is None:
            filters = []
        if constraints is None:
            constraints = []
        if mappers is None:
            mappers = []
        if reducers is None:
            reducers = []
        if emitter is None:
            emitter = self.default_emitter
        if getfirst_exception is None:
            getfirst_exception = self.default_getfirst_exception
        self._filters = filters
        self._constraints = constraints
        self._mappers = mappers
        self._reducers = reducers
        self._emitter = emitter
        self._getfirst = getfirst
        self._getfirst_exception = getfirst_exception
        self._fallback = fallback
        self._init_constraints()

    def __call__(self):
        result = self._map_reduce(
            self._values,
            mappers=self._effective_mappers,
            reducers=self._effective_reducers,
            emitter=self._emitter,
            getfirst=self._getfirst,
            getfirst_exception=self._getfirst_exception,
            fallback=self._fallback)
        return result

    # Protected

    _map_reduce = map_reduce

    @property
    @abstractmethod
    def _values(self):
        pass  # pragma: no cover

    @property
    def _effective_mappers(self):
        mappers = []
        for constraint in self._effective_constraints:
            if constraint:
                mappers.append(constraint)
        mappers += self._mappers
        return mappers

    @property
    def _effective_reducers(self):
        return self._reducers

    @property
    def _effective_filters(self):
        return self._filters

    @property
    def _effective_constraints(self):
        return self._constraints

    def _init_constraints(self):
        for effective_filter in self._effective_filters:
            for name, value in effective_filter.items():
                for constraint in self._effective_constraints:
                    constraint.extend(name, value)


class FindEmitter(Emitter):
    """Emitter representation for find framework.
    """

    # Public

    pass
