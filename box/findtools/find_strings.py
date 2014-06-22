from functools import partial
from ..dependency import inject
from ..itertools import map_reduce
from ..os import enhanced_join
from ..types import RegexCompiledPatternType
from .find_files import FindFilesEmitter
from .not_found import NotFound
  
class find_strings(map_reduce):
    """Find strings in files using map_reduce framework.
    
    :param str/re string: string filter
    :param list files: list of filepathes where to find
    :param str basedir: base directory to find
    
    :returns mixed: map_reduce result
    
    Function also accepts :class:`box.itertools.map_reduce` kwargs.
    """
    
    #Public
    
    default_emitter = inject('box.findtools.find_strings.FindStringsEmitter')    
    
    def __init__(self, string=None, *, 
                 files=[], basedir=None, **kwargs):
        self._string = string
        self._files = files
        self._basedir = basedir
        super().__init__(**kwargs) 
    
    #Protected
        
    _getfirst_exception = NotFound
    _open = staticmethod(open)
    
    @property
    def _extension_values(self):
        for filepath in self._files:
            #Reads every file from find_files
            full_filepath = enhanced_join(self._basedir, filepath)
            partial_emitter = partial(self._emitter, 
                filepath=filepath, basedir=self._basedir)
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
    

class FindStringsEmitter(FindFilesEmitter): pass     