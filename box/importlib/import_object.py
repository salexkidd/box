import importlib

def import_object(name, package=None):
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