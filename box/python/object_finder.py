import re
from importlib.machinery import SourceFileLoader
from .file_finder import FileFinder
from .map_reduce import MapReduce
from .regex_types import RegexCompiledPatternType

class ObjectFinder:
    
    #Public
    
    #TODO: add ignore_errors flag
    def find(self, name=None, filename=None, basedir='.', max_depth=0, 
             breakers=[], filters=[], processors=[], reducers=[]):
        filters = [self._name_filter_class(name)]+filters
        objects = self._get_objects(filename, basedir, max_depth)
        map_reduce = MapReduce(breakers, filters, processors, reducers)
        map_reduced_objects = map_reduce(objects)
        return map_reduced_objects
    
    #Protected
    
    _name_filter_class = property(lambda self: ObjectFinderNameFilter)
    _source_file_loader_class = SourceFileLoader
    _file_finder_class = FileFinder    
    
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
        file_finder = self._file_finder_class()
        files = file_finder.find(filename, basedir, max_depth)
        return files
    
        
class ObjectFinderNameFilter:
    
    #Public
    
    def __init__(self, name):
        self._name = name
        
    def __call__(self, obj, name, module):
        if self._name:
            pattern = self._name
            if not isinstance(pattern, RegexCompiledPatternType):
                pattern = re.compile(pattern)
            if not pattern.match(name):
                return False
        return True        