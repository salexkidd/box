from ..functools import cachedproperty, FunctionCall 
from .environment import EnvironmentMixin

class render_string(FunctionCall):
    """Render a string using context.
    
    :param str source: string to be rendered
    :param dict/obj context: rendering context
    :param str target: filepath to write renered string into
    :param object loader: jinja2's loader    
    :param dict env_params: parameters to pass to jinja2's Environment
    
    :returns str/None: rendered string
    
    If target is given function will not return any value.   
    """
    
    #Public
    
    def __init__(self, source, context={}, *, 
                 target=None, loader=None, **env_params):
        self._source = source
        self._context = context
        self._target = target
        self._loader = loader
        self._env_params = env_params
    
    def __call__(self):
        content = self._render()
        if self._target:
            self._write(content)
        else:
            return content
            
    #Protected
    
    _open = staticmethod(open)
    
    def _render(self):
        return self._template.render(self._context)
    
    def _write(self, content):
        with self._open(self._target, 'w') as file:
            file.write(content)
                
    @cachedproperty
    def _template(self):
        environment = self._environment_class(
            loader=self._loader, **self._env_params)
        return environment.from_string(self._source)
    
    @property
    def _environment_class(self):
        from jinja2 import Environment
        class Environment(EnvironmentMixin, Environment): pass
        return Environment