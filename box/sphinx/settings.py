from ..functools import cachedproperty
from ..importlib import import_object
from ..packaging import Settings, include
from .setup import setup


class Settings(Settings):
    """Sphinx conf.py representation.

    Just put code like this in conf.py module and use inheritance from
    default sphinx settings and other class benefits. It gives a opportunity
    to not operate with big config file filled by standard settings and
    see only important things::

      from box.sphinx import Settings

      class Settings(Settings):

          # Documentation:
          # http://sphinx-doc.org/config.html

          # Project

          project = 'box'

      locals().update(Settings())
    """

    # Public

    def __getattr__(self, name):
        try:
            return getattr(self._defaults, name)
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

    # Setup

    @property
    def setup(self):
        @include
        def esetup(app):
            # Sphinx doesn't work with bound method
            for name in sorted(dir(self)):
                attr = getattr(self, name)
                item = getattr(attr, setup.attribute_name, None)
                if item is not None:
                    item.invoke(self, app)
        return esetup

    # Protected

    @cachedproperty
    def _defaults(self):
        Config = import_object('sphinx.config.Config')
        return Config(None, None, {}, None)
