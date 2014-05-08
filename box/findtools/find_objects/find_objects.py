from importlib.machinery import SourceFileLoader
from ...itertools import map_reduce
from ...os import enhanced_join
from ..find_files import find_files
from ..not_found import NotFound
from .emitter import FindObjectsEmitter
from .objname import FindObjectsObjnameMapper
from .objtype import FindObjectsObjtypeMapper
 
class find_objects(map_reduce):
    
    #Public  
    
    default_emitter = FindObjectsEmitter
       
    def __init__(self, objname=None, objtype=None, *, 
                 filename=None, filepath=None,  
                 basedir=None, maxdepth=None,
                 onwalkerror=None, **kwargs):
        self._objname = objname
        self._objtype = objtype
        self._filename = filename        
        self._filepath = filepath
        self._basedir = basedir
        self._maxdepth = maxdepth       
        self._onwalkerror = onwalkerror
        super().__init__(**kwargs)            
    
    #Protected
    
    _getfirst_exception = NotFound    
    _loader_class = SourceFileLoader
    _find_files = staticmethod(find_files)
    
    @property
    def _extension_values(self):
        for filepath in self._filepathes:
            #Loads as a module every file from find_files 
            full_filepath = enhanced_join(self._basedir, filepath)
            loader = self._loader_class(full_filepath, full_filepath)
            module = loader.load_module(full_filepath)
            for objname in dir(module):
                #Emits every object in module
                obj = getattr(module, objname)
                yield self._emitter(obj, 
                    object=obj, objname=objname, module=module,
                    basedir=self._basedir, filepath=filepath)

    @property
    def _extension_mappers(self):
        return [FindObjectsObjnameMapper(self._objname),
                FindObjectsObjtypeMapper(self._objtype)] 
     
    @property             
    def _filepathes(self):
        files = self._find_files(
            filename=self._filename,
            filepath=self._filepath,             
            basedir=self._basedir, 
            maxdepth=self._maxdepth,
            onwalkerror = self._onwalkerror)
        return files            