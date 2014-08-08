import os
from ..functools import Function, cachedproperty
from ..importlib import inject
from ..itertools import map_reduce, Emitter
from ..glob import enhanced_iglob
from ..os import balanced_walk, enhanced_join
from ..types import RegexCompiledPatternType
from .not_found import NotFound
from .maxdepth import MaxdepthConstraint
from .filename import FilenameConstraint
from .filepath import FilepathConstraint


class find_files(Function):
    """Find files using map_reduce framework.

    :param list filters: find filters
    :param str basedir: base directory to find
    :param bool join: if True joins resulted filepath with basedir
    :param dict params: map_reduce params

    :returns mixed: map_reduced files
    """

    # Public

    default_emitter = inject('FindFilesEmitter', module=__name__)
    default_getfirst_exception = NotFound

    def __init__(self, *filters,
                 basedir=None, filepath=None, join=False, **params):
        params.setdefault('emitter', self.default_emitter)
        params.setdefault(
            'getfirst_exception',
            self.default_getfirst_exception)
        self._filters = filters
        self._basedir = basedir
        self._filepath = filepath
        self._join = join
        self._params = params
        self._init_constraints()

    def __call__(self):
        files = self._map_reduce(
            self._values,
            mappers=self._effective_mappers, **self._params)
        return files

    # Protected

    _map_reduce = map_reduce
    _glob = staticmethod(enhanced_iglob)
    _walk = staticmethod(balanced_walk)

    @cachedproperty
    def _values(self):
        for filepath in self._filepathes:
            # Emits every file in filepathes
            file = filepath
            if self._join:
                file = enhanced_join(self._basedir, filepath)
            yield self._emitter(
                file, filepath=filepath, basedir=self._basedir)

    @cachedproperty
    def _effective_mappers(self):
        mappers = []
        for constraint in self._constraints:
            if constraint:
                mappers.append(constraint)
        mappers += self._mappers
        return mappers

    @cachedproperty
    def _filepathes(self):
        if (self._filepath is None or
            isinstance(self._filepath, RegexCompiledPatternType)):
            # We have to walk
            filepathes = self._walk(
                basedir=self._basedir, sorter=sorted, mode='files')
        else:
            # We have a glob pattern
            filepathes = self._glob(
                self._filepath,
                basedir=self._basedir, sorter=sorted, mode='files')
        return filepathes

    @cachedproperty
    def _constraints(self):
        constraints = [
            MaxdepthConstraint(),
            FilenameConstraint(),
            FilepathConstraint(self._basedir)]
        return constraints

    def _init_constraints(self):
        for name, value in self._filters:
            for constraint in self._constraints:
                constraint.extend(name, value)


class FindFilesEmitter(Emitter):
    """Emitter representation for find_files.

    Additional attributes:

    - filepath
    - basedir
    """

    # Public

    @property
    def filename(self):
        return os.path.basename(self.filepath)
