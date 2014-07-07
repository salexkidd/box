from importlib.machinery import SourceFileLoader
from ..dependency import inject
from ..itertools import map_reduce
from ..os import enhanced_join
from .find_files import find_files, FindFilesEmitter
from .not_found import NotFound
from .objname import ObjnameConstraint
from .objtype import ObjtypeConstraint
 
#TODO: finilize error handling
class find_objects(map_reduce):
    """Find objects in files using map_reduce framework.
    
    :param str/re objname: include objname
    :param str/re notobjname: exclude objname
    :param type objtype: include objtype
    :param type notobjtype: exclude objtype    
    :param str basedir: base directory to find
    :param list files: list of filepathes where to find
    :param callable onimporterror: error handler for import [NOT IMPLEMENTED]
    
    Arguments for find_files if files == None:
    
    :param str/glob/re filename: include filenames
    :param str/glob/re notfilename: exclude filenames
    :param str/glob/re filepath: include filepathes
    :param str/glob/re notfilepath: exclude filepathes
    :param int maxdepth: maximal find depth relatively to basedir
    :param callable onwalkerror: error handler for os.walk
    
    :returns mixed: map_reduce result    
    
    Function also accepts :class:`box.itertools.map_reduce` kwargs.
    """
    
    #Public  
    
    default_emitter = inject('FindObjectsEmitter', module=__name__)
       
    def __init__(self, *,
                 objname=None, notobjname=None,
                 objtype=None, notobjtype=None,
                 basedir=None, files=None, onimporterror=None, 
                 filename=None, notfilename=None, 
                 filepath=None, notfilepath=None,
                 maxdepth=None, onwalkerror=None,
                 **kwargs):
        self._objname = ObjnameConstraint(objname, notobjname)
        self._objtype = ObjtypeConstraint(objtype, notobjtype)
        self._basedir = basedir
        self._files = files
        self._onimporterror = onimporterror
        self._filename = filename
        self._notfilename = notfilename
        self._filepath = filepath
        self._notfilepath = notfilepath
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
                    filepath=filepath, basedir=self._basedir)

    @property
    def _extension_mappers(self):
        return [self._objname,
                self._objtype]
                    
    @property
    def _filepathes(self):
        if self._files != None:
            #We have ready files
            return self._files
        else:                   
            #We have to find files
            files = self._find_files(
                filename=self._filename,
                notfilename=self._notfilename,
                filepath=self._filepath,
                notfilepath=self._notfilepath,
                basedir=self._basedir,
                maxdepth=self._maxdepth,
                onwalkerror=self._onwalkerror)
            return files
    
    
class FindObjectsEmitter(FindFilesEmitter): 

    #Public
    
    @property
    def objtype(self):
        return type(self.object)    