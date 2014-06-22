import importlib

def import_object(name, *, module=None, package=None):
    """Import an object.
    
    :param str/mixed name: 
      object name in "[module.]module.]attr" form
      
    :param str module:
      anchor point from which to resolve attribute
    
    :param str package: 
      argument is required when performing a relative import. 
      It specifies the package to use as the anchor point from which 
      to resolve the relative import to an absolute import
      
    :raises ValueError: 
      if name is a string but not in a proper form
      
    :returns object/mixed: 
      imported object
      
    If name not is a string function returns name without changes.
    It usefull when client may give you pointer to some objects in 
    two forms like string or already imported object::
    
      >>> obj = import_object('box.importlib.import_object')
      >>> obj is import_object(obj)
      >>> obj
      <function box.importlib.import_object.import_object>
    """
    if isinstance(name, str):
        if module != None:
            name = '.'.join([module, name])
        try:
            module, name = name.rsplit('.', 1)
        except ValueError:
            raise ValueError('Name is in a bad form.') from None
        imported_module = importlib.import_module(module, package=package)
        imported_object = getattr(imported_module, name)
    else:
        imported_object = name
    return imported_object