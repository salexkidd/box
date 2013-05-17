import importlib
from .virtual_package import VirtualPackage

def import_module(name, path=None):
    package = None
    if name.startswith('.'):
        if not path:
            raise TypeError('Relative import requires path')
        package = VirtualPackage(path).__name__
    return importlib.import_module(name, package)