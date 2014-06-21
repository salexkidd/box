from importlib.machinery import SourceFileLoader
from ..itertools import map_reduce
from ..os import enhanced_join
from .find_files import find_files, FindFilesEmitter
from .not_found import NotFound
from .objname import ObjnameMapper
from .objtype import ObjtypeMapper
 
class find_objects(map_reduce):
    """Find objects in files using map_reduce framework.
    
    :param str/re objname: objname filter
    :param type objtype: objtype filter    
    :param list files: list of filepathes where to find
    :param str basedir: base directory to find
    
    :returns mixed: map_reduce result    
    
    Function also accepts :class:`box.itertools.map_reduce` kwargs.
    """
    
    #Public  
    
    default_emitter = property(lambda self: FindObjectsEmitter)
       
    def __init__(self, objname=None, objtype=None, *, 
                 files=[], basedir=None, **kwargs):
        self._objname = objname
        self._objtype = objtype
        self._files = files
        self._basedir = basedir
        super().__init__(**kwargs)            
    
    #Protected
    
    _getfirst_exception = NotFound    
    _loader_class = SourceFileLoader
    _find_files = staticmethod(find_files)
    
    @property
    def _extension_values(self):
        for filepath in self._files:
            #Loads as a module every file from find_files 
            full_filepath = enhanced_join(self._basedir, filepath)
            loader = self._loader_class(full_filepath, full_filepath)
            module = loader.load_module(full_filepath)
            for objname in dir(module):
                #Emits every object in module
                obj = getattr(module, objname)
                yield self._emitter(obj, 
                    object=obj, objname=objname, module=module,
                    filepath=filepath, basedir=self._basedir)

    @property
    def _extension_mappers(self):
        return [ObjnameMapper(self._objname),
                ObjtypeMapper(self._objtype)]
    
    
class FindObjectsEmitter(FindFilesEmitter): 

    #Public
    
    @property
    def objtype(self):
        return type(self.object)    