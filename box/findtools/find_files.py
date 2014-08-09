import os
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


class find_files(Function):
    """Find files using map_reduce framework.

    :param list filters: find filters
    :param bool join: if True joins resulted filepath with basedir
    :param str basedir: base directory to find
    :param list filepathes: list of filepathes or globs where to find
    :param dict params: map_reduce params

    :returns mixed: map_reduced files
    """

    # Public

    default_emitter = inject('FindFilesEmitter', module=__name__)
    default_getfirst_exception = NotFound

    def __init__(self, *filters, join=False,
                 basedir=None, filepathes=None, **params):
        params.setdefault('emitter', self.default_emitter)
        params.setdefault(
            'getfirst_exception',
            self.default_getfirst_exception)
        self._filters = filters
        self._basedir = basedir
        self._filepathes = filepathes
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
        for constraint in self._constraints:
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
    def _constraints(self):
        constraints = [
            MaxdepthConstraint(),
            FilenameConstraint(),
            FilepathConstraint(self._basedir)]
        return constraints

    def _init_constraints(self):
        for filter_item in self._filters:
            for name, value in filter_item.items():
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
