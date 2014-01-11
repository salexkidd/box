import re
from .file_finder import FileFinder
from .map_reduce import MapReduce

class StringFinder:
    
    #Public
    
    #TODO: add ignore_errors flag
    def find(self, pattern, filename=None, basedir='.', max_depth=0, 
             breakers=[], filters=[], processors=[], reducers=[]):
        file_finder = self._file_finder_class()
        file_finder_reducer = self._file_finder_reducer_class(
            pattern, breakers, filters, processors, reducers)
        map_reduced_strings = file_finder.find(
            filename, basedir, max_depth, reducers=[file_finder_reducer])
        return map_reduced_strings
    
    #Protected
    
    _file_finder_class = FileFinder
    _file_finder_reducer_class = property(
        lambda self: StringFinderFileFinderReducer)
    
    
class StringFinderFileFinderReducer:
    
    #Public
    
    def __init__(self, pattern, 
                 breakers=[], filters=[], processors=[], reducers=[]):
        self._pattern = pattern
        self._breakers = breakers
        self._filters = filters
        self._processors = processors
        self._reducers = reducers
        
    def __call__(self, files):
        strings = self._get_strings(files)
        map_reduce = MapReduce(
            self._breakers, self._filters, self._processors, self._reducers)
        map_reduced_strins = map_reduce(strings)
        return map_reduced_strins
    
    #Protected
    
    _open_operator = staticmethod(open)
    
    def _get_strings(self, files):
        for file in files:
            with self._open_operator(file) as file_object:
                pattern = self._pattern
                if not self._is_object_regexp_compiled_pattern(pattern):
                    pattern = re.compile(pattern)
                strings = pattern.findall(file_object.read())
                for string in strings:
                    yield (string, file)
    
    def _is_object_regexp_compiled_pattern(self, obj):
        return isinstance(obj, type(re.compile('')))                  