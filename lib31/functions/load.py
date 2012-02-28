import sys
import types
from ..types.runtime_package import RuntimePackage

class load(object):
    """
    Type: function-like class
    Usage: load(pointer, direct=load.DIRECT, path=[])
    
    Returns pointer if pointer type in direct,
    imports module if pointer is module name or
    imports attribute from module if pointer is module.object.
        
    Uses path as additional path to find module 
    without sys.path affecting (runtime package).
    """
    
    DIRECT = [
        types.ModuleType, 
        type,
    ]
    
    def __new__(cls, pointer, direct=DIRECT, path=[]):
        if not cls._check_pointer_type_in_direct(pointer, direct):
            return cls._import_by_pointer(pointer, path)
        else:
            return pointer
        
    @staticmethod
    def _check_pointer_type_in_direct(pointer, direct):
        for item in direct:
            if isinstance(pointer, item):
                return True
        else:
            return False
        
    @classmethod
    def _import_by_pointer(cls, pointer, path=[]):
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
    def _import(name, path=[]):
        try:
            __import__(name)
        except ImportError:
            if path:
                package = RuntimePackage(path)
                name = '.'.join([package.__name__, name])
                __import__(name)
            else:
                raise
        return sys.modules[name]