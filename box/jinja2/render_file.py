import os
from ..functools import cachedproperty 
from .render_string import render_string

class render_file(render_string):
    """Render a file using context.
    
    :param str source: filepath to be rendered    
    
    .. seealso:: Full documentation: :class:`box.jinja2.render_string`    
    """
    
    #Protected
                
    @cachedproperty
    def _template(self):
        source = self._source
        loader = self._loader
        if not loader:
            dirpath, source = os.path.split(self._source)
            loader = self._file_system_loader_class(dirpath)
        environment = self._environment_class(loader=loader)          
        return environment.get_template(source)
    
    @property
    def _file_system_loader_class(self):
        from jinja2 import FileSystemLoader
        return FileSystemLoader