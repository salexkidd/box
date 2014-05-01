import inspect      
from ..find_files import FindFilesEmitter    
    
class FindObjectsEmitter(FindFilesEmitter):

    #Public

    @property
    def filepath(self):
        return inspect.getfile(self.module)