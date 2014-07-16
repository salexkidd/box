from copy import copy as python_copy

def enhanced_copy(obj, *args, **kwargs):
    """Shallow copy operation on arbitrary Python objects.

    :param mixed obj: object to copy
    :param tuple args: args to pass to object's __copy__ method
    :param dict kwargs: kwargs to pass to object's __copy__ method

    Difference with python library module is in __copy__ method priority:

      - if object has __copy__ method function calls it with args and kwarg
      - if object hasn't __copy__ method function acts like copy.copy
    """
    if hasattr(obj, '__copy__'):
        return obj.__copy__(*args, **kwargs)
    else:
        return python_copy(obj)
