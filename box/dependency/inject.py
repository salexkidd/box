from ..importlib import import_object

def inject(name, package=None):
    """Return imported object wrapped in property.
    
    .. seealso:: :func:`box.importlib.import_object`
    """
    obj = import_object(name, package=package)
    prop = property(lambda self: obj)
    return prop