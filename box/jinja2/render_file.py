import os
from ..functools import FunctionCall
from .environment import EnvironmentMixin

class render_file(FunctionCall):
    
    #Public
    
    def __init__(self, source, context={}, *, target=None):
        self._source = source
        self._context = context
        self._target = target
    
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
                
    @property
    def _template(self):
        dirpath, filename = os.path.split(self._source)
        loader = self._file_system_loader_class(dirpath)
        environment = self._environment_class(loader=loader)
        template = environment.get_template(filename)    
        return template
    
    @property
    def _file_system_loader_class(self):
        from jinja2 import FileSystemLoader
        return FileSystemLoader
    
    @property
    def _environment_class(self):
        from jinja2 import Environment
        class Environment(EnvironmentMixin, Environment): pass
        return Environment