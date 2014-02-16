import inspect
from importlib.machinery import SourceFileLoader
from ..types import RegexCompiledPatternType
from .find_files import find_files, FindFilesMapEmitter
from .find import find
 
class find_objects(find):
    
    #Public  
    
    default_basedir = '.'
    default_emitter = 'deferred:FindObjectsMapEmitter'
       
    def __init__(self, objname=None, objtype=None, *, 
                 filename=None, filepath=None,  
                 basedir=None, maxdepth=None, 
                 mappers=[], reducers=[], emitter=None, 
                 fallback=None, onwalkerror=None, followlinks=False):
        self._objname = objname
        self._objtype = objtype
        self._filename = filename        
        self._filepath = filepath        
        self._basedir = basedir
        self._maxdepth = maxdepth
        self._user_mappers = mappers
        self._user_reducers = reducers
        self._emitter = emitter
        self._fallback = fallback        
        self._onwalkerror = onwalkerror
        self._followlinks = followlinks          
        if not self._basedir:
            self._basedir = self.default_basedir
        if not self._emitter:
            self._emitter = self.default_emitter
    
    #Protected
    
    _source_file_loader_class = SourceFileLoader
    _find_files_function = staticmethod(find_files)
    
    @property
    def _iterable(self):
        for module in self._modules:
            for objname in dir(module):
                obj = getattr(module, objname)
                yield self._emitter(obj,
                    object=obj, 
                    objname=objname, 
                    module=module)
    
    @property              
    def _modules(self):
        for file in self._files: 
            loader = self._source_file_loader_class(file, file)
            module = loader.load_module(file)
            yield module   
     
    @property             
    def _files(self):
        files = self._find_files_function(
            filename=self._filename,
            filepath=self._filepath,             
            basedir=self._basedir, 
            maxdepth=self._maxdepth,
            onwalkerror = self._onwalkerror,
            followlinks = self._followlinks)
        return files

    @property
    def _builtin_mappers(self):
        return [FindObjectsObjnameMapper(self._objname),
                FindObjectsObjtypeMapper(self._objtype)] 
         
    
class FindObjectsMapEmitter(FindFilesMapEmitter):

    #Public

    @property
    def filepath(self):
        return inspect.getfile(self.module)
   
        
class FindObjectsObjnameMapper:
    
    #Public
    
    def __init__(self, objname):
        self._objname = objname
        
    def __call__(self, emitter):
        if self._objname:
            if isinstance(self._objname, RegexCompiledPatternType):
                if not self._objname.match(emitter.objname):
                    emitter.skip()
            else:
                if emitter.objname != self._objname:
                    emitter.skip()
                    

class FindObjectsObjtypeMapper:
    
    #Public
    
    def __init__(self, objtype):
        self._objtype = objtype
        
    def __call__(self, emitter):
        if self._objtype:
            types = self._objtype
            if isinstance(types, type):
                types = [types]
            if not isinstance(emitter.object, tuple(types)):
                emitter.skip()
                
                
find_objects.default_emitter = FindObjectsMapEmitter                 