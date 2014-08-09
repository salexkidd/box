from importlib.machinery import SourceFileLoader
from ..functools import cachedproperty
from ..importlib import inject
from ..itertools import map_reduce
from ..os import enhanced_join
from .find_files import find_files, FindFilesEmitter
from .not_found import NotFound
from .objname import ObjnameConstraint
from .objtype import ObjtypeConstraint


class find_objects(map_reduce):
    """Find objects in files using map_reduce framework.

    :param list filters: find filters
    :param str basedir: base directory to find
    :param list filepathes: list of filepathes or globs where to find
    :param dict params: map_reduce params

    :returns mixed: map_reduce result
    """

    # Public

    default_emitter = inject('FindObjectsEmitter', module=__name__)
    default_getfirst_exception = NotFound

    def __init__(self, *filters,
                 basedir=None, filepathes=None, **params):
        params.setdefault('emitter', self.default_emitter)
        params.setdefault(
            'getfirst_exception',
            self.default_getfirst_exception)
        self._filters = filters
        self._basedir = basedir
        self._filepathes = filepathes
        self._params = params
        self._init_constraints()

    def __call__(self):
        objects = self._map_reduce(
            self._values,
            mappers=self._effective_mappers, **self._params)
        return objects

    # Protected

    _find_files = staticmethod(find_files)
    _map_reduce = map_reduce
    _SourceFileLoader = SourceFileLoader

    @cachedproperty
    def _values(self):
        for filepath in self._effective_filepathes:
            # Loads as a module every file in filepathes
            full_filepath = enhanced_join(self._basedir, filepath)
            loader = self._SourceFileLoader(full_filepath, full_filepath)
            module = loader.load_module(full_filepath)
            for objname in dir(module):
                # Emits every object in module
                obj = getattr(module, objname)
                yield self._emitter(
                    obj, object=obj, objname=objname, module=module,
                    filepath=filepath, basedir=self._basedir)

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
        filepathes = self._find_files(
            *self._filters,
            basedir=self._basedir,
            filepathes=self._filepathes)
        return filepathes

    @cachedproperty
    def _constraints(self):
        constraints = [
            ObjnameConstraint(),
            ObjtypeConstraint()]
        return constraints

    def _init_constraints(self):
        for filter_item in self._filters:
            for name, value in filter_item.items():
                for constraint in self._constraints:
                    constraint.extend(name, value)


class FindObjectsEmitter(FindFilesEmitter):
    """Emitter representation for find_objects.

    Additional attributes:

    - object
    - objname
    - module
    - filepath
    - basedir
    """

    # Public

    @property
    def objtype(self):
        return type(self.object)
