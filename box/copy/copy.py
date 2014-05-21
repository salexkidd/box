from copy import copy as python_copy

def copy(obj, *args, **kwargs):
    """Shallow copy operation on arbitrary Python objects.
    
    :param mixed obj: object to copy
    :param tuple args: args to pass to object's __copy__ method
    :param dict kwargs: kwargs to pass to object's __copy__ method      
    
    If object has __copy__ method function calls it with args and kwarg.
    If object hasn't __copy__ method function acts like copy.copy.
    """
    if hasattr(obj, '__copy__'):
        return obj.__copy__(*args, **kwargs)
    else:
        return python_copy(object)