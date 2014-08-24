import os
from ..functools import cachedproperty
from .render_string import render_string


class render_file(render_string):
    """Render a file using context.

    Parameters
    ----------
    source: str
        Filepath to be rendered.

    .. seealso:: Full documentation: :class:`box.jinja2.render_string`
    """

    # Protected

    @cachedproperty
    def _template(self):
        source = self._source
        loader = self._loader
        if not loader:
            dirpath, source = os.path.split(self._source)
            loader = self._FileSystemLoader(dirpath)
        environment = self._Environment(
            loader=loader, **self._env_params)
        return environment.get_template(source)

    @property
    def _FileSystemLoader(self):
        return self._jinja2.FileSystemLoader
