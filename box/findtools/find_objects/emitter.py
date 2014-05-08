from ..find_files import FindFilesEmitter    
    
class FindObjectsEmitter(FindFilesEmitter): 

    #Public
    
    @property
    def objtype(self):
        return type(self._object)