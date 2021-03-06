from importlib import import_module
from ..collections import Settings, include
from ..functools import cachedproperty
from .setup import setup
from .connect import connect


class Settings(Settings):
    """Sphinx conf.py representation.

    Examples
    --------
    Just put code like this in conf.py module and use inheritance from
    default sphinx settings and other class benefits. It gives an opportunity
    to not operate with big config file filled by standard settings and
    see only important things::

      import sphinx
      from box.sphinx import Settings

      class Settings(Settings):

          # Documentation:
          # http://sphinx-doc.org/config.html

          # Project

          project = 'box'

      locals().update(Settings(sphinx=sphinx))
    """

    # Public

    def __init__(self, *args, sphinx, **kwargs):
        self._sphinx = sphinx
        super().__init__(*args, **kwargs)

    def __getattr__(self, name):
        try:
            return getattr(self.__defaults, name)
        except AttributeError:
            raise AttributeError(name)

    # Project

    @property
    def release(self):
        return self.version

    # LaTeX

    @property
    def latex_documents(self):
        return [(
            self.master_doc,
            self.project + '.tex',
            self.project + ' Documentation',
            self.author,
            'manual')]

    # Manual

    @property
    def man_pages(self):
        return [(
            self.master_doc,
            self.project,
            self.project + ' Documentation',
            [self.author],
            1)]

    # Texinfo

    @property
    def texinfo_documents(self):
        return [(
            self.master_doc,
            self.project,
            self.project + ' Documentation',
            self.author,
            self.project,
            'One line description of project.',
            'Miscellaneous')]

    # Autodoc

    @connect('autodoc-process-docstring')
    def autodoc_process_docstring(self, app, what, name, obj, options, lines):
        if what != 'module':
            for key, value in enumerate(lines):
                if key >= 1 and value.startswith('---'):
                    lines[key - 1] = lines[key - 1].join(['**', '**'])
                    lines[key] = ''

    @connect('autodoc-skip-member')
    def autodoc_skip_member(self, app, what, name, obj, skip, options):
        return skip or (name in getattr(self, 'autodoc_skip_members', []))

    # Setup

    @property
    def setup(self):
        @include
        def esetup(app):
            # Sphinx doesn't work with bound method
            for cls in type(self).mro():
                for name, value in vars(cls).items():
                    decorator = getattr(value, setup.decorator, None)
                    if decorator is None:
                        continue
                    function = getattr(self, name)
                    decorator.invoke(function, app)
        return esetup

    # Private

    @cachedproperty
    def __defaults(self):
        return self.__sphinx_config.Config(None, None, {}, None)

    @property
    def __sphinx_config(self):
        return import_module('.config', package=self._sphinx.__name__)
