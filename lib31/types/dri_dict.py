import copy
from .managed_dict import ManagedDict         
            
class DRIDict(ManagedDict):
    """
    Initiates from DEFAULT, 
    mutates with checking REQUIRED and IMMUTABLE
    """
    
    DEFAULT = {}
    REQUIRED = []
    IMMUTABLE = []
    
    def __init__(self, init=None):
        data = copy.deepcopy(self.DEFAULT)
        if init:
            data.update(init)                          
        super(DRIDict, self).__init__(data)

    def __delitem__(self, key):
        if key in self.REQUIRED:
            raise KeyError('{key} is required'.
                           format(key=key))
        else:
            super(DRIDict, self).__delitem__(key)

    def __setitem__(self, key, value):
        if key in self.IMMUTABLE and key in self:
            raise KeyError('{key} is immutable'.
                           format(key=key))
        else:
            super(DRIDict, self).__setitem__(key, value)