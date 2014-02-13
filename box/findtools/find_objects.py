from importlib.machinery import SourceFileLoader
from ..functools import FunctionCall
from ..itertools import map_reduce, MapEmmiter
from ..types import RegexCompiledPatternType
from .find_files import find_files   
    
class find_objects(FunctionCall):
    
    #Public  
    
    default_basedir = '.' 
   
    def __init__(self, attrname=None, filename=None, basedir=None, 
                 max_depth=None, mappers=[], reducers=[]):
        self._attrname = attrname
        self._filename = filename
        self._basedir = basedir
        self._max_depth = max_depth
        self._mappers = mappers
        self._reducers = reducers
        if not self._basedir:
            self._basedir = self.default_basedir
    
    def __call__(self):
        objects = self._get_objects()
        mappers = self._builtin_mappers+self._mappers
        result = map_reduce(objects, mappers, self._reducers)
        return result
    
    #Protected
    
    _source_file_loader_class = SourceFileLoader
    _find_files_function = staticmethod(find_files)    
    
    def _get_objects(self):
        for module in self._get_modules():
            for attrname in dir(module):
                obj = getattr(module, attrname)
                yield MapEmmiter(obj, object=obj, attrname=attrname, module=module)
                    
    def _get_modules(self):
        for file in self._get_files(): 
            loader = self._source_file_loader_class(file, file)
            module = loader.load_module(file)
            yield module   
                    
    def _get_files(self):
        files = self._find_files_function(
            self._filename, self._basedir, self._max_depth)
        return files
    
    @property
    def _builtin_mappers(self):
        return [FindObjectsAttrnameMapper(self._attrname)]
    
        
class FindObjectsAttrnameMapper:
    
    #Public
    
    def __init__(self, attrname):
        self._attrname = attrname
        
    def __call__(self, emitter):
        if self._attrname:
            if isinstance(self._attrname, RegexCompiledPatternType):
                if not self._attrname.match(emitter.attrname):
                    emitter.skip()
            else:
                if emitter.attrname != self._attrname:
                    emitter.skip()