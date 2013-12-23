from types import ModuleType

def remove_modules(scope, skip=[]):
    """Remove all module objects from scope 
       except ones with key in skip list"""
    for key, attr in list(scope.items()):
        if (isinstance(attr, ModuleType) and 
            key not in skip):
            del scope[key]