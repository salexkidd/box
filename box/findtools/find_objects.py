from importlib.machinery import SourceFileLoader
from ..itertools import map_reduce
from ..os import enhanced_join
from .find_files import find_files, FindFilesEmitter
from .not_found import NotFound
from .objname import ObjnameMapper
from .objtype import ObjtypeMapper
 
class find_objects(map_reduce):
    """Find objects in files using map_reduce framework.
    
    :param str/re objname: objname filter
    :param type objtype: objtype filter    
    :param str/glob/re filename: filename filter
    :param str/glob/re filepath: filepath filter
    :param str basedir: base directory to find
    :param int maxdepth: maximal find depth relatively to basedir
    :param callable onwalkerror: error handler for os.walk
    
    :returns generator: found objects generator    
    
    Function also accepts :class:`box.itertools.map_reduce` kwargs.
    """
    
    #Public  
    
    default_emitter = property(lambda self: FindObjectsEmitter)
       
    def __init__(self, objname=None, objtype=None, *, 
                 filename=None, filepath=None,  
                 basedir=None, maxdepth=None,
                 onwalkerror=None, **kwargs):
        self._objname = objname
        self._objtype = objtype
        self._filename = filename        
        self._filepath = filepath
        self._basedir = basedir
        self._maxdepth = maxdepth       
        self._onwalkerror = onwalkerror
        super().__init__(**kwargs)            
    
    #Protected
    
    _getfirst_exception = NotFound    
    _loader_class = SourceFileLoader
    _find_files = staticmethod(find_files)
    
    @property
    def _extension_values(self):
        for filepath in self._filepathes:
            #Loads as a module every file from find_files 
            full_filepath = enhanced_join(self._basedir, filepath)
            loader = self._loader_class(full_filepath, full_filepath)
            module = loader.load_module(full_filepath)
            for objname in dir(module):
                #Emits every object in module
                obj = getattr(module, objname)
                yield self._emitter(obj, 
                    object=obj, objname=objname, module=module,
                    basedir=self._basedir, filepath=filepath)

    @property
    def _extension_mappers(self):
        return [ObjnameMapper(self._objname),
                ObjtypeMapper(self._objtype)] 
     
    @property             
    def _filepathes(self):
        files = self._find_files(
            filename=self._filename,
            filepath=self._filepath,             
            basedir=self._basedir, 
            maxdepth=self._maxdepth,
            onwalkerror = self._onwalkerror)
        return files
    
    
class FindObjectsEmitter(FindFilesEmitter): 

    #Public
    
    @property
    def objtype(self):
        return type(self.object)    