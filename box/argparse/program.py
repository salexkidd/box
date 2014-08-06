from abc import ABCMeta, abstractmethod
from ..functools import cachedproperty
from .command import Command
from .settings import Settings

class Program(metaclass=ABCMeta):
    """Abstract console program representation.

    :param list argv: sys.argv like list of arguments

    Client have to implement __call__ method and can adjust
    _Command and _Settings attributes using replacements
    compatible with module's :class:`box.argparse.Command`,
    :class:`box.argparse.Settings`.

    Usage exmaple::

      >>> from box.argparse import Program, Settings
      >>> class Settings(Settings):
      ...   argparse = {'arguments': [{'name': 'arguments', 'nargs':'*'}]}
      >>> class Program(Program):
      ...   def __call__(self):
      ...     print(self._command.arguments)
      ...   _Settings = Settings
      >>> program = Program(['program', 'arg'])
      >>> program()
      ['arg']
    """

    # Public

    def __init__(self, argv):
        self._argv = argv

    @abstractmethod
    def __call__(self):
        pass  # pragma: no cover

    # Protected

    _Command = Command
    _Settings = Settings

    @cachedproperty
    def _command(self):
        return self._Command(
            self._argv, config=self._settings.argparse)

    @cachedproperty
    def _settings(self):
        return self._Settings()
