from ...itertools import map_reduce
from ...types import RegexCompiledPatternType
from ..find_files import find_files
from ..not_found import NotFound
from .emitter import FindStringsEmitter
  
class find_strings(map_reduce):

    #Public
    
    default_basedir = '.'
    default_emitter = FindStringsEmitter
    
    def __init__(self, string=None, *,
                 filename=None, filepath=None,  
                 basedir=None, maxdepth=None,
                 onwalkerror=None, **kwargs):
        self._string = string
        self._filename = filename
        self._filepath = filepath        
        self._basedir = basedir
        self._maxdepth = maxdepth
        self._onwalkerror = onwalkerror
        if not self._basedir:
            self._basedir = self.default_basedir
        super().__init__(**kwargs) 
    
    #Protected
        
    _getfirst_exception = NotFound        
    _open = staticmethod(open)
    _find_files = staticmethod(find_files)
    
    @property
    def _extension_values(self):
        for filepath in self._files:
            #Reads every file selected by find_files
            with self._open(filepath) as fileobj:
                filetext = fileobj.read()
                if isinstance(self._string, RegexCompiledPatternType):
                    #Search string is regex object - re search
                    for match in self._string.finditer(filetext):
                        matched_groups = match.groups()
                        if matched_groups:
                            #Emits every matched group
                            for matched_group in matched_groups:
                                yield self._emitter(matched_group, 
                                                    filepath=filepath)
                        else:
                            #Emits whole match
                            matched_string = match.group()
                            yield self._emitter(matched_string, 
                                                filepath=filepath)
                elif self._string:
                    #Search string is string - str search
                    matches = filetext.count(self._string)
                    for _ in range(matches):
                        #Emits given strings matches count times
                        yield self._emitter(self._string, filepath=filepath)
                else:
                    #Search string is None - no search
                    #Emits whole file
                    yield self._emitter(filetext, filepath=filepath)
                    
    @property
    def _files(self):
        files = self._find_files(
            filename=self._filename,
            filepath=self._filepath,
            basedir=self._basedir, 
            maxdepth=self._maxdepth,
            onwalkerror = self._onwalkerror)
        return files