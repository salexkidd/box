from ..functools import cachedproperty, FunctionCall 
from .environment import EnvironmentMixin

class render_string(FunctionCall):
    
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
        environment = self._environment_class(loader=self._loader)
        return environment.from_string(self._source)
    
    @property
    def _environment_class(self):
        from jinja2 import Environment
        class Environment(EnvironmentMixin, Environment): pass
        return Environment