from .import_module import import_module

def import_attribute(name, path=None):
    try:
        module_name, attr_name = name.rsplit('.', 1)
    except ValueError:
        raise TypeError('Name requires to be in [.]module.attr form')
    module = import_module(module_name, path)
    attr = getattr(module, attr_name)
    return attr