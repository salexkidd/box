import importlib

def check_module(name, package=None):
    """Check module is available for importing.
    
    Arguments the same importlib.import_module has.
    """
    try:
        importlib.import_module(name, package)
    except ImportError:
        return False
    else:
        return True
