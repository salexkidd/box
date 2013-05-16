import importlib
from .virtual_package import VirtualPackage

def import_module(name, path=None):
    if path:
        pass
    else:
        return importlib.import_module(name)