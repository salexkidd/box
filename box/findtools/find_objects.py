from importlib.machinery import SourceFileLoader
from ..functools import cachedproperty
from ..os import enhanced_join
from .emitter import FindObjectsEmitter
from .find import find
from .find_files import find_files
from .objname import ObjnameConstraint
from .objtype import ObjtypeConstraint


class find_objects(find):
    """Find objects in files using map_reduce framework.

    :param list filters: find filters
    :param str basedir: base directory to find
    :param list filepathes: list of filepathes or globs where to find
    :param dict params: map_reduce params

    :returns mixed: map_reduce result
    """

    # Public

    default_emitter = FindObjectsEmitter

    def __init__(self, *,
                 basedir=None, filepathes=None, **find_params):
        self._basedir = basedir
        self._filepathes = filepathes
        super().__init__(**find_params)

    # Protected

    _find_files = staticmethod(find_files)
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
    def _effective_constraints(self):
        constraints = [
            ObjnameConstraint(),
            ObjtypeConstraint()]
        constraints += super()._effective_constraints
        return constraints

    @cachedproperty
    def _effective_filepathes(self):
        filepathes = self._find_files(
            basedir=self._basedir,
            filepathes=self._filepathes,
            filters=self._filters)
        return filepathes
