from ..itertools import map_reduce
from ..types import RegexCompiledPatternType
from .find_files import find_files

class FindStrings:
    
    #Public
    
    BREAK_BEFORE = map_reduce.BREAK_BEFORE
    BREAK_AFTER = map_reduce.BREAK_AFTER
    
    #TODO: add ignore_errors flag
    def __call__(self, string, filename=None, basedir='.', max_depth=None, 
             breakers=[], filters=[], processors=[], reducers=[]):
        strings = self._get_strings(string, filename, basedir, max_depth)
        map_reduced_strings = map_reduce(
            strings, breakers, filters, processors, reducers)
        return map_reduced_strings
    
    #Protected
    
    _open_function = staticmethod(open)
    _find_files_function = staticmethod(find_files)
    
    def _get_strings(self, string, filename, basedir, max_depth):
        for file in self._get_files(filename, basedir, max_depth):
            with self._open_function(file) as file_object:
                file_content = file_object.read()
                if isinstance(string, RegexCompiledPatternType):
                    for match in string.finditer(file_content):
                        has_groups = bool(match.groups())
                        yield (match.group(has_groups), file)
                else:
                    matches = file_content.count(string)
                    for _ in range(matches+1):
                        yield (string, file)
                    
    def _get_files(self, filename, basedir, max_depth):
        files = self._find_files_function(filename, basedir, max_depth)
        return files  
    
    
find_strings = FindStrings()               