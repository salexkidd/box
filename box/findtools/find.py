import os
from abc import ABCMeta, abstractmethod
from itertools import chain
from ..functools import Function, cachedproperty
from ..importlib import inject
from ..itertools import map_reduce, Emitter
from ..glob import enhanced_iglob
from ..os import balanced_walk, enhanced_join
from .not_found import NotFound
from .maxdepth import MaxdepthConstraint
from .filename import FilenameConstraint
from .filepath import FilepathConstraint


class find(Function, metaclass=ABCMeta):
    """Find framework base class.
    """

    # Public

    default_emitter = inject('FindEmitter', module=__name__)
    default_getfirst_exception = NotFound

    def __init__(self, *,
                 filters=None, constraints=None,
                 mappers=[], reducers=[], emitter=None,
                 getfirst=False, getfirst_exception=None, fallback=None):
        if filters is None:
            filters = []
        if constraints is None:
            constraints = []
        if emitter is None:
            emitter = self.default_emitter
        if getfirst_exception is None:
            emitter = self.default_getfirst_exception
        self._filters = filters
        self._constraints = constraints
        self._mappers = mappers
        self._reducers = reducers
        self._emitter = emitter
        self._getfirst = getfirst
        self._getfirst_exception = getfirst_exception
        self._fallback = fallback

    def __call__(self):
        files = self._map_reduce(
            self._values,
            mappers=self._effective_mappers,
            **self._params)
        return files

    # Protected

    _map_reduce = map_reduce
    _glob = staticmethod(enhanced_iglob)
    _walk = staticmethod(balanced_walk)

    @cachedproperty
    def _values(self):
        for filepath in self._effective_filepathes:
            # Emits every file in filepathes
            file = filepath
            if self._join:
                file = enhanced_join(self._basedir, filepath)
            yield self._params['emitter'](
                file, filepath=filepath, basedir=self._basedir)

    @cachedproperty
    def _effective_mappers(self):
        mappers = []
        for constraint in self._effective_constraints:
            if constraint:
                mappers.append(constraint)
        mappers += self._params.pop('mappers', [])
        return mappers

    @cachedproperty
    def _effective_filepathes(self):
        if self._filepathes is not None:
            # We have pathes or globs
            # TODO: fix it's not LAZY load
            chunks = []
            for filepath in self._filepathes:
                chunk = self._glob(
                    filepath,
                    basedir=self._basedir,
                    sorter=sorted,
                    mode='files')
                chunks.append(chunk)
            filepathes = chain(*chunks)
        else:
            # We have to walk fully
            filepathes = self._walk(
                basedir=self._basedir,
                sorter=sorted,
                mode='files')
        return filepathes

    @cachedproperty
    def _effective_constraints(self):
        constraints = [
            MaxdepthConstraint(),
            FilenameConstraint(),
            FilepathConstraint(self._basedir)]
        constraints += self._constraints
        return constraints

    def _init_constraints(self):
        for filter_item in self._filters:
            for name, value in filter_item.items():
                for constraint in self._effective_constraints:
                    constraint.extend(name, value)


class FindEmitter(Emitter):
    """Emitter representation for find framework.
    """

    # Public

    pass
