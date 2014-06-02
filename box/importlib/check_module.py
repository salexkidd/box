import importlib

def check_module(name, package=None):
    """Check module is available for importing.
    """
    try:
        importlib.import_module(name, package)
    except ImportError:
        return False
    else:
        return True 