import os
from ..functools import Null

def enhanced_join(*components, skip_none=True, fallback=Null):
    """Enhanced version of os.path.join.

    :param str component: path component to join
    :param bool skip_none: skip if None in components
    :param mixed fallback: if join fails return fallback
    """
    try:
        if skip_none:
            components = filter(
                lambda component: component != None, components)
        return os.path.join(*components)
    except Exception:
        if fallback != Null:
            return fallback
        else:
            raise
