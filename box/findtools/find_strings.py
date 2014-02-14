from ..functools import FunctionCall
from ..itertools import map_reduce, MapEmmiter
from ..types import RegexCompiledPatternType
from .find_files import find_files    
    
class find_strings(FunctionCall):

    #Public
    
    default_basedir = '.'
    
    def __init__(self, string=None, *,
                 filename=None, filepath=None,  
                 basedir=None, maxdepth=None, 
                 mappers=[], reducers=[]):
        self._string = string
        self._filename = filename
        self._filepath = filepath        
        self._basedir = basedir
        self._maxdepth = maxdepth
        self._mappers = mappers
        self._reducers = reducers
        if not self._basedir:
            self._basedir = self.default_basedir
            
    def __call__(self):
        strings = self._get_strings()
        values = map_reduce(strings, self._mappers, self._reducers)
        return values
    
    #Protected
        
    _open_function = staticmethod(open)
    _find_files_function = staticmethod(find_files)
    
    def _get_strings(self):
        for filepath in self._get_files():
            with self._open_function(filepath) as fileobj:
                filetext = fileobj.read()
                if isinstance(self._string, RegexCompiledPatternType):
                    for match in self._string.finditer(filetext):
                        has_groups = bool(match.groups())
                        matched_string = match.group(has_groups)
                        yield MapEmmiter(matched_string, filepath=filepath)
                elif self._string:
                    matches = filetext.count(self._string)
                    for _ in range(matches):
                        yield MapEmmiter(self._string, filepath=filepath)
                else:
                    yield MapEmmiter(filetext, filepath=filepath)
                    
    def _get_files(self):
        files = self._find_files_function(
            filename=self._filename,
            filepath=self._filepath,
            basedir=self._basedir, 
            maxdepth=self._maxdepth)
        return files             