from importlib.machinery import SourceFileLoader
from ...itertools import map_reduce
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
    _source_file_loader_class = SourceFileLoader
    _find_files = staticmethod(find_files)
    
    @property
    def _extension_values(self):
        for file in self._files:
            #Loads as a module every selected by find_files file 
            loader = self._source_file_loader_class(file, file)
            module = loader.load_module(file)
            for objname in dir(module):
                #Gets every object in module
                obj = getattr(module, objname)
                #Emits gotten object
                yield self._emitter(obj,
                    object=obj, 
                    objname=objname,
                    module=module)

    @property
    def _extension_mappers(self):
        return [FindObjectsObjnameMapper(self._objname),
                FindObjectsObjtypeMapper(self._objtype)] 
     
    @property             
    def _files(self):
        files = self._find_files(
            filename=self._filename,
            filepath=self._filepath,             
            basedir=self._basedir, 
            maxdepth=self._maxdepth,
            onwalkerror = self._onwalkerror,
            join=True)
        return files            