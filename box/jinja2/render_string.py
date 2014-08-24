import os
import sys
from unittest.mock import patch
from importlib import import_module
from ..copy import enhanced_copy
from ..functools import cachedproperty, Function
from .context import ObjectContext


class render_string(Function):
    """Render a string using context.

    If target is given function will not return any value.

    Parameters
    ----------
    source: str
        String to be rendered.
    context: dict/obj
        Rendering context.
    target: str
        Filepath to write renered string into.
    loader: object
        Jinja2's loader.
    env_params: dict
        Parameters to pass to jinja2's Environment.

    Returns
    -------
    str/None
        Rendered string.
    """

    # Public

    def __init__(self, source, context=None, *,
                 jinja2, target=None, loader=None, **env_params):
        if context is None:
            context = {}
        self._source = source
        self._context = context
        self._jinja2 = jinja2
        self._target = target
        self._loader = loader
        self._env_params = env_params

    def __call__(self):
        content = self._render()
        if self._target:
            self._write(content)
        else:
            return content

    # Protected

    def _render(self):
        with patch.object(
            self._jinja2_runtime, 'new_context', self._new_context):
            return self._template.render(self._context)

    def _write(self, content):
        dirname = os.path.dirname(self._target)
        if dirname:
            os.makedirs(dirname, exist_ok=True)
        with open(self._target, 'w') as file:
            file.write(content)

    @cachedproperty
    def _template(self):
        environment = self._Environment(
            loader=self._loader, **self._env_params)
        return environment.from_string(self._source)

    @cachedproperty
    def _Environment(self):
        class Environment(self._jinja2.Environment):
            # Public
            template_class = self._Template
        return Environment

    @cachedproperty
    def _Template(self):
        new_context = self._new_context
        concat = self._jinja2_utils.concat
        class Template(self._jinja2.Template):
            # Public
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

    def _new_context(self, environment, template_name, blocks,
                     vrs=None, shared=None, globs=None, locs=None):
        if vrs is None:
            vrs = {}  # pragma: no cover; TODO: try to remove?
        parent = vrs
        if not isinstance(vrs, dict):
            parent = ObjectContext(vrs)
        if not shared:
            parent = enhanced_copy(parent)
            for key, value in (globs or {}).items():
                if key not in parent:
                    # dict.setdefault doesn't work for ObjectContext
                    parent[key] = value
        if locs:
            if shared:
                parent = enhanced_copy(parent)
            for key, value in locs.items():
                if (key[:2] == 'l_' and
                    value is not self._jinja2_runtime.missing):
                    parent[key[2:]] = value
        return self._jinja2_runtime.Context(
            environment, parent, template_name, blocks)

    @property
    def _jinja2_utils(self):
        return import_module('.utils', package=self._jinja2.__name__)

    @property
    def _jinja2_runtime(self):
        return import_module('.runtime', package=self._jinja2.__name__)
