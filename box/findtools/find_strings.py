from functools import partial
from ..dependency import inject
from ..itertools import map_reduce
from ..os import enhanced_join
from ..types import RegexCompiledPatternType
from .find_files import FindFilesEmitter, find_files
from .not_found import NotFound
  
class find_strings(map_reduce):
    """Find strings in files using map_reduce framework.
    
    :param str/re string: string filter
    :param str basedir: base directory to find
    :param list files: list of filepathes where to find
    
    Arguments for find_files if files == None:
    
    :param str/glob/re filename: include filenames
    :param str/glob/re notfilename: exclude filenames
    :param str/glob/re filepath: include filepathes
    :param str/glob/re notfilepath: exclude filepathes
    :param int maxdepth: maximal find depth relatively to basedir
    
    :returns mixed: map_reduce result
    
    Function also accepts :class:`box.itertools.map_reduce` kwargs.
    """
    
    #Public
    
    default_emitter = inject('FindStringsEmitter', module=__name__)    
    
    def __init__(self, string=None, *, 
                 basedir=None, files=None, 
                 filename=None, notfilename=None, 
                 filepath=None, notfilepath=None,
                 maxdepth=None,
                 **kwargs):
        self._string = string
        self._basedir = basedir
        self._files = files
        self._filename = filename
        self._notfilename = notfilename
        self._filepath = filepath
        self._notfilepath = notfilepath
        self._maxdepth = maxdepth
        super().__init__(**kwargs) 
    
    #Protected
        
    _getfirst_exception = NotFound
    _find_files = staticmethod(find_files)
    _open = staticmethod(open)
    
    @property
    def _system_values(self):
        for filepath in self._effective_files:
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
                    
    @property
    def _effective_files(self):
        if self._files != None:
            #We have ready files
            return self._files
        else:                   
            #We have find files
            files = self._find_files(
                filename=self._filename,
                notfilename=self._notfilename,
                filepath=self._filepath,
                notfilepath=self._notfilepath,
                basedir=self._basedir,
                maxdepth=self._maxdepth)
            return files


class FindStringsEmitter(FindFilesEmitter): pass     