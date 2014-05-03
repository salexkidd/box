import importlib

def import_object(name, package=None):
    """Import an object.
    
    :param str/mixed name: 
      object name in "[module.]module.attr" form
    
    :param object package: argument is required when performing 
      a relative import. It specifies the package to use as the anchor point
      from which to resolve the relative import to an absolute import
      
    :raises ValueError: 
      if name is a string but not in proper form
      
    :returns object/mixed: 
      object by name
      
    If name not is a string function returns name without changes.
    It usefull when client may give you pointer to some objects in 
    two forms like string or already imported object:
    
    >>> obj = import_object('box.importlib.import_object')
    >>> obj is import_object(obj)
    >>> obj
    <function box.importlib.import_object.import_object>
    """
    if isinstance(name, str):
        try:
            module_name, attribute_name = name.rsplit('.', 1)
        except ValueError:
            raise ValueError('Name format not is [.]module.attr')
        module = importlib.import_module(module_name, package)
        attribute = getattr(module, attribute_name)
    else:
        attribute = name
    return attribute