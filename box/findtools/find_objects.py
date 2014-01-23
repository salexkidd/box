from importlib.machinery import SourceFileLoader
from ..itertools import map_reduce
from ..types import RegexCompiledPatternType
from .find_files import find_files

class FindObjects:
    
    #Public  
    
    default_basedir = '.' 
    
    def __call__(self, name=None, filename=None, basedir=None, max_depth=None, 
             breakers=[], filters=[], processors=[], reducers=[]):
        if not basedir:
            basedir = self.default_basedir        
        filters = [self._name_filter_class(name)]+filters
        objects = self._get_objects(filename, basedir, max_depth)
        map_reduced_objects = map_reduce(
            objects, breakers, filters, processors, reducers)
        return map_reduced_objects
    
    #Protected
    
    _name_filter_class = property(lambda self: FindObjectsNameFilter)
    _source_file_loader_class = SourceFileLoader
    _find_files_function = staticmethod(find_files)    
    
    def _get_objects(self, filename, basedir, max_depth):
        for module in self._get_modules(filename, basedir, max_depth):
            for name in dir(module):
                obj = getattr(module, name)
                yield (obj, name, module)
                    
    def _get_modules(self, filename, basedir, max_depth):
        for file in self._get_files(filename, basedir, max_depth): 
            loader = self._source_file_loader_class(file, file)
            module = loader.load_module(file)
            yield module   
                    
    def _get_files(self, filename, basedir, max_depth):
        files = self._find_files_function(filename, basedir, max_depth)
        return files
    
        
class FindObjectsNameFilter:
    
    #Public
    
    def __init__(self, name):
        self._name = name
        
    def __call__(self, obj, name, module):
        if self._name:
            if isinstance(self._name, RegexCompiledPatternType):
                if not self._name.match(name):
                    return False
            else:
                if name != self._name:
                    return False
        return True
    

find_objects = FindObjects()