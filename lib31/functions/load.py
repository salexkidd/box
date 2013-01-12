import sys
import types
from ..types.fake_package import FakePackage

class Load(object):
    """
    Load function class.
    """
    
    #Public
    
    direct = [
        types.ModuleType, 
        type,
    ]
    
    def __call__(self, pointer, direct=direct, path=None):
        """
        Loads module or module attribute.
        
        Arguments:
          - pointer: str
          - direct: list = load.direct
          - path: list = None, uses path instead sys.path 
            without sys.path affecting (fake package)
        
        Returns:
          - pointer if pointer type in direct
          - module if pointer is module name
          - attribute from module if pointer is module.object
        
        Raises:
          - TypeError if path is not a list
          - ImportError if import fallen
        """
        if path and not isinstance(path, list):
            raise TypeError('Path must be a list like sys.path')        
        if not self._check_pointer_type_in_direct(pointer, direct):
            return self._import_by_pointer(pointer, path=path)
        else:
            return pointer
    
    #Protected
        
    @staticmethod
    def _check_pointer_type_in_direct(pointer, direct):
        for item in direct:
            if isinstance(pointer, item):
                return True
        else:
            return False
            
    @classmethod    
    def _import_by_pointer(cls, pointer, path=None):
        splited = pointer.rsplit('.', 1)
        module_name = splited.pop(0)
        module = cls._import(module_name, path=path)
        try:
            attr_name = splited.pop(0)
            attr = getattr(module, attr_name)
            return attr          
        except IndexError:
            return module        

    @staticmethod
    def _import(name, path=None):
        if path:
            package = FakePackage(path)
            name = '.'.join([package.__name__, name])
        __import__(name)
        return sys.modules[name]
    
    
load = Load()