import re
from .file_finder import FileFinder
from .map_reduce import MapReduce

class ObjectFinder:
    
    #Public
    
    #TODO: add ignore_errors flag
    def find(self, attrname=None, filename=None, basedir='.', max_depth=0, 
             breakers=[], filters=[], processors=[], reducers=[]):
        strings = self._get_strings(attrname, filename, basedir, max_depth)
        map_reduce = MapReduce(breakers, filters, processors, reducers)
        map_reduced_strings = map_reduce(strings)
        return map_reduced_strings
    
    #Protected
    
    _open_operator = staticmethod(open)
    _file_finder_class = FileFinder    
    
    def _get_strings(self, pattern, filename, basedir, max_depth):
        for file in self._get_files(filename, basedir, max_depth):
            with self._open_operator(file) as file_object:
                if not self._is_object_regexp_compiled_pattern(pattern):
                    pattern = re.compile(pattern)
                strings = pattern.findall(file_object.read())
                for string in strings:
                    yield (string, file)
                    
    def _get_files(self, filename, basedir, max_depth):
        file_finder = self._file_finder_class()
        files = file_finder.find(filename, basedir, max_depth)
        return files
    
    def _is_object_regexp_compiled_pattern(self, obj):
        return isinstance(obj, type(re.compile('')))
    
        
class AttrnameObjectFinderFilter:
    
    #Public
    
    def __init__(self, attrname):
        self._attrname = attrname
        
    def __call__(self, file):
        depth = self._calculate_depth(file)
        if depth > self._max_depth:
            return True 
        return False       