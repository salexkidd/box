from .file_finder import FileFinder
from .map_reduce import MapReduce
from .regex_types import RegexCompiledPatternType

class StringFinder:
    
    #Public
    
    #TODO: add ignore_errors flag
    def find(self, string, filename=None, basedir='.', max_depth=0, 
             breakers=[], filters=[], processors=[], reducers=[]):
        strings = self._get_strings(string, filename, basedir, max_depth)
        map_reduce = MapReduce(breakers, filters, processors, reducers)
        map_reduced_strings = map_reduce(strings)
        return map_reduced_strings
    
    #Protected
    
    _open_operator = staticmethod(open)
    _file_finder_class = FileFinder
    
    def _get_strings(self, string, filename, basedir, max_depth):
        for file in self._get_files(filename, basedir, max_depth):
            with self._open_operator(file) as file_object:
                #TODO: read line by line someway!?
                #TODO: finditer?
                file_content = file_object.read()
                if isinstance(string, RegexCompiledPatternType):
                    strings = string.findall(file_content)
                else:
                    strings = string*file_content.count(string)
                for strng in strings:
                    yield (strng, file)
                    
    def _get_files(self, filename, basedir, max_depth):
        file_finder = self._file_finder_class()
        files = file_finder.find(filename, basedir, max_depth)
        return files                 