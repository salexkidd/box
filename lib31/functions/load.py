import sys

class load(object):
    """
    Imports module or object from module. 
    """
    
    def __new__(cls, pointer, direct=[type], path=[]):
        """
        Returns pointer if pointer type in direct,
        imports module if pointer is module name or
        imports object from module if pointer is module.object.
        
        Just for import time sys.path = path + sys.path.
        """
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
        
    @staticmethod
    def _import_by_pointer(pointer, path=[]):        
        sys.path = path + sys.path
        splited = pointer.rsplit('.', 1)
        name = splited.pop(0)
        try:
            attr = splited.pop(0)
            obj = getattr(__import__(name, fromlist=[attr]), attr)
        except IndexError:
            obj = __import__(name)
        sys.path = sys.path[len(path):]
        return obj       