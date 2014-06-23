from ..importlib import import_object

def inject(name, *, module=None, package=None):
    """Return imported object wrapped in property.
    
    .. seealso:: :func:`box.importlib.import_object`
    """
    return property(lambda self: 
        import_object(name, module=module, package=package))