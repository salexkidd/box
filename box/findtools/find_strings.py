from ..itertools import map_reduce, MapEmmiter
from ..types import RegexCompiledPatternType
from .find_files import find_files

class FindStrings:

    #Public
        
    def __call__(self, *args, **kwargs):
        call = self._call_class(*args, **kwargs)
        result = call.execute()
        return result
    
    #Protected
    
    _call_class = property(lambda self: FindStringsCall)
    
    
class FindStringsCall:

    #Public
    
    default_basedir = '.'
    
    def __init__(self, string, filename=None, basedir=None, max_depth=None, 
             mappers=[], reducers=[]):
        self._string = string
        self._filename = filename
        self._basedir = basedir
        self._max_depth = max_depth
        self._mappers = mappers
        self._reducers = reducers
        if not self._basedir:
            self._basedir = self.default_basedir
            
    def execute(self):
        strings = self._get_strings()
        values = map_reduce(strings, self._mappers, self._reducers)
        return values
    
    #Protected
        
    _open_function = staticmethod(open)
    _find_files_function = staticmethod(find_files)
    
    def _get_strings(self):
        for file in self._get_files():
            with self._open_function(file) as file_object:
                file_content = file_object.read()
                if isinstance(self._string, RegexCompiledPatternType):
                    for match in self._string.finditer(file_content):
                        has_groups = bool(match.groups())
                        yield MapEmmiter(match.group(has_groups), file=file)
                else:
                    matches = file_content.count(self._string)
                    for _ in range(matches+1):
                        yield MapEmmiter(self._string, file=file)
                    
    def _get_files(self):
        files = self._find_files_function(
            self._filename, self._basedir, self._max_depth)
        return files             
    
    
find_strings = FindStrings()               