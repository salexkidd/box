import os
from ..functools import Function
from .render_string import render_string


class render_dir(Function):
    """Render a directory using context.

    Directory rendering means that every name from os.listdir
    will be processed by render_string and then renamed accordingly.

    Parameters
    ----------
    source: str
        Directory to be rendered.
    context: dict/obj
        Rendering context.
    env_params: dict
        Parameters to pass to render_string.
    """

    # Public

    def __init__(self, source, context=None, **env_params):
        if context is None:
            context = {}
        self._source = source
        self._context = context
        self._env_params = env_params

    def __call__(self):
        for name in os.listdir(self._source):
            try:
                new_name = render_string(
                    name, self._context, **self._env_params)
                if name != new_name:
                    path = os.path.join(self._source, name)
                    new_path = os.path.join(self._source, new_name)
                    os.rename(path, new_path)
            except Exception:
                pass
