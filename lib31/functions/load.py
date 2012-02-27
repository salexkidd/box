import sys
import types
from ..types.runtime_package import RuntimePackage

class load(object):
    """
    Type: function
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
        if path:
            package = RuntimePackage(path)
            module_name = ('{package}.{module}'.format(
                package=package.__name__,
                module=module_name,
            ))
        module = cls._import_by_name(module_name)
        try:
            attr_name = splited.pop(0)
            attr = getattr(module, attr_name)
            return attr          
        except IndexError:
            return module
        
    @staticmethod
    def _import_by_name(name):
        __import__(name)
        return sys.modules[name]