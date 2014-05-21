import sys
from unittest.mock import patch
from collections.abc import Mapping
from ..copy import copy
from ..functools import cachedproperty, FunctionCall 
from .context import ObjectContext

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
        with patch('jinja2.runtime.new_context', self._new_context):
            return self._template.render(self._context)
    
    def _write(self, content):
        with self._open(self._target, 'w') as file:
            file.write(content)
                
    @cachedproperty
    def _template(self):
        environment = self._environment_class(
            loader=self._loader, **self._env_params)
        return environment.from_string(self._source)
    
    @cachedproperty
    def _environment_class(self):
        from jinja2 import Environment
        class Environment(Environment):
            #Public
            template_class = self._template_class
        return Environment
    
    @cachedproperty
    def _template_class(self):
        from jinja2 import Template
        from jinja2.utils import concat
        new_context = self._new_context
        class Template(Template):
            #Public
            def render(self, context):
                try:
                    context = self.new_context(context)
                    return concat(self.root_render_func(context))
                except Exception:
                    exc_info = sys.exc_info()
                return self.environment.handle_exception(exc_info, True)
            def new_context(self, vrs=None, shared=False, locs=None):
                return new_context(
                    self.environment, self.name, self.blocks,
                    vrs, shared, self.globals, locs)
        return Template     
    
    @staticmethod
    def _new_context(environment, template_name, blocks, 
                     vrs=None, shared=None, globs=None, locs=None):
        from jinja2.runtime import Context, missing
        if vrs is None:
            vrs = {}
        if isinstance(vrs, Mapping):
            parent = vrs
            if not shared:
                #TODO: make for ObjectContext
                parent = dict(globs or (), **vrs)
        else:            
            parent = ObjectContext(vrs)
        if locs:
            if shared:
                parent = copy(parent)
            for key, value in locs.items():
                if key[:2] == 'l_' and value is not missing:
                    parent[key[2:]] = value
        return Context(environment, parent, template_name, blocks)  