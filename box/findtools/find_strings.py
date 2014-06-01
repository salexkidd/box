from functools import partial
from ..itertools import map_reduce
from ..os import enhanced_join
from ..types import RegexCompiledPatternType
from .find_files import find_files, FindFilesEmitter
from .not_found import NotFound
  
class find_strings(map_reduce):
    """Find strings in files using map_reduce framework.
    
    :param str/re string: string filter
    :param str/glob/re filename: filename filter
    :param str/glob/re filepath: filepath filter
    :param str basedir: base directory to find
    :param int maxdepth: maximal find depth relatively to basedir
    :param callable onwalkerror: error handler for os.walk
    
    Function also accepts :class:`box.itertools.map_reduce` kwargs.
    """
    
    #Public
    
    default_emitter = property(lambda self: FindStringsEmitter)
    
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
        super().__init__(**kwargs) 
    
    #Protected
        
    _getfirst_exception = NotFound        
    _open = staticmethod(open)
    _find_files = staticmethod(find_files)
    
    @property
    def _extension_values(self):
        for filepath in self._filepathes:
            #Reads every file from find_files
            partial_emitter = partial(self._emitter, 
                basedir=self._basedir, filepath=filepath)
            full_filepath = enhanced_join(self._basedir, filepath)
            with self._open(full_filepath) as fileobj:
                filetext = fileobj.read()
                if isinstance(self._string, RegexCompiledPatternType):
                    #Search string is regex object - re search
                    for match in self._string.finditer(filetext):
                        matched_groups = match.groups()
                        if matched_groups:
                            #Emits every matched group
                            for matched_group in matched_groups:
                                yield partial_emitter(matched_group)
                        else:
                            #Emits whole match
                            matched_string = match.group()
                            yield partial_emitter(matched_string)
                elif self._string:
                    #Search string is string - str search
                    matches = filetext.count(self._string)
                    for _ in range(matches):
                        #Emits given strings matches count times
                        yield partial_emitter(self._string)
                else:
                    #Search string is None - no search
                    #Emits whole file
                    yield partial_emitter(filetext)
                    
    @property
    def _filepathes(self):
        files = self._find_files(
            filename=self._filename,
            filepath=self._filepath,
            basedir=self._basedir, 
            maxdepth=self._maxdepth,
            onwalkerror = self._onwalkerror)
        return files
    

class FindStringsEmitter(FindFilesEmitter): pass     