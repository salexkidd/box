import os
from ..functools import FunctionCall
from .render_string import render_string

class render_dir(FunctionCall):
    """Render a directory using context.
    
    :param str source: directory to be rendered
    :param dict/obj context: rendering context
    
    Directory rendering means that every name from os.listdir
    will be processed by render_string and then renamed accordingly. 
    
    .. note:: This class acts like a function when called.    
    """
    
    #Public
    
    def __init__(self, source, context={}):
        self._source = source
        self._context = context
    
    def __call__(self):
        for name in os.listdir(self._source):
            try:
                new_name = render_string(name, self._context)
                if name != new_name:
                    path = os.path.join(self._source, name)
                    new_path = os.path.join(self._source, new_name)
                    os.rename(path, new_path)
            except Exception:
                pass         