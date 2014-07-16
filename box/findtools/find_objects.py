from importlib.machinery import SourceFileLoader
from ..dependency import inject
from ..functools import cachedproperty
from ..itertools import map_reduce
from ..os import enhanced_join
from .find_files import find_files, FindFilesEmitter
from .not_found import NotFound
from .objname import ObjnameConstraint
from .objtype import ObjtypeConstraint

class find_objects(map_reduce):
    """Find objects in files using map_reduce framework.
    
    :param str/re objname: include objnames pattern
    :param str/re notobjname: exclude objnames pattern
    :param type objtype: include objtypes pattern
    :param type notobjtype: exclude objtypes pattern  
    :param str basedir: base directory to find
    :param list filepathes: list of filepathes where to find
    
    Arguments for find_files if filepathes == None:
    
    :param str/glob/re filename: include filenames pattern
    :param str/glob/re notfilename: exclude filenames pattern
    :param str/glob/re filepath: include filepathes pattern
    :param str/glob/re notfilepath: exclude filepathes pattern
    :param int maxdepth: maximal find depth relatively to basedir
    
    :returns mixed: map_reduce result    
    
    Function also accepts :class:`box.itertools.map_reduce` kwargs.
    """

    # Public

    default_emitter = inject('FindObjectsEmitter', module=__name__)

    def __init__(self, *,
                 objname=None, notobjname=None,
                 objtype=None, notobjtype=None,
                 basedir=None, filepathes=None,
                 filename=None, notfilename=None,
                 filepath=None, notfilepath=None,
                 maxdepth=None,
                 **kwargs):
        self._objname = objname
        self._notobjname = notobjname
        self._objtype = objtype
        self._notobjtype = notobjtype
        self._basedir = basedir
        self._filepathes = filepathes
        self._filename = filename
        self._notfilename = notfilename
        self._filepath = filepath
        self._notfilepath = notfilepath
        self._maxdepth = maxdepth
        super().__init__(**kwargs)

    # Protected

    _getfirst_exception = NotFound
    _loader_class = SourceFileLoader
    _find_files = staticmethod(find_files)

    @cachedproperty
    def _system_values(self):
        for filepath in self._effective_filepathes:
            # Loads as a module every file in filepathes
            full_filepath = enhanced_join(self._basedir, filepath)
            loader = self._loader_class(full_filepath, full_filepath)
            module = loader.load_module(full_filepath)
            for objname in dir(module):
                # Emits every object in module
                obj = getattr(module, objname)
                yield self._emitter(obj,
                    object=obj, objname=objname, module=module,
                    filepath=filepath, basedir=self._basedir)

    @cachedproperty
    def _system_mappers(self):
        mappers = []
        objname = ObjnameConstraint(self._objname, self._notobjname)
        if objname:
            mappers.append(objname)
        objtype = ObjtypeConstraint(self._objtype, self._notobjtype)
        if objtype:
            mappers.append(objtype)
        return mappers

    @cachedproperty
    def _effective_filepathes(self):
        if self._filepathes != None:
            # We have ready filepathes
            return self._filepathes
        else:
            # We have to find filepathes
            filepathes = self._find_files(
                filename=self._filename,
                notfilename=self._notfilename,
                filepath=self._filepath,
                notfilepath=self._notfilepath,
                basedir=self._basedir,
                maxdepth=self._maxdepth)
            return filepathes


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
