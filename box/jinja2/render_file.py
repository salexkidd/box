import os
from ..functools import cachedproperty, FunctionCall 
from .environment import EnvironmentMixin

class render_file(FunctionCall):
    
    #Public
    
    def __init__(self, source, context={}, *, loader=None, target=None):
        self._source = source
        self._context = context
        self._target = target
        self._loader = loader
    
    def __call__(self):
        content = self._render()
        self._write(content)
        return content
            
    #Protected
    
    _open_function = staticmethod(open)
    
    def _render(self):
        return self._template.render(self._context)
    
    def _write(self, content):
        if self._target:
            with self._open_function(self._target, 'w') as file:
                file.write(content)
                
    @cachedproperty
    def _template(self):
        return self._environment.get_template(self._effective_source)    
    
    @cachedproperty
    def _environment(self):
        return self._environment_class(loader=self._effective_loader)
    
    @cachedproperty
    def _effective_source(self):
        if self._loader:
            return self._source
        else:
            return os.path.basename(self._source)
            
    @cachedproperty
    def _effective_loader(self):
        if self._loader:
            return self._loader
        else:
            dirpath = os.path.dirname(self._source)
            return self._file_system_loader_class(dirpath)
    
    @property
    def _file_system_loader_class(self):
        from jinja2 import FileSystemLoader
        return FileSystemLoader
    
    @property
    def _environment_class(self):
        from jinja2 import Environment
        class Environment(EnvironmentMixin, Environment): pass
        return Environment