import os
from copy import copy
from ..collections import merge_dicts
from ..functools import cachedproperty
from .parser import Parser


# TODO: fix protected/private
class Command:
    """Console command representation.

    Parameters
    ----------
    argv: list
        Program's arguments like sys.argv.
    config: dict
        Command configuration for argparse.
    exception: :class:`Exception`
        Exception class to raise instead of exit.
    kwargs: dict
        Pairs of key=value to configure command over config.

    Examples
    --------
    Command provides access to command line arguments by attribute names::

      >>> from box.argparse import Command
      >>> config = {'arguments': [{'name': 'arguments', 'nargs':'*'}]}
      >>> command = Command(['program', 'arg'], config=config)
      >>> command.arguments
      ['arg']
    """

    # Public

    def __init__(self, argv, *, config, exception=None, **kwargs):
        self._argv = argv
        self._config = merge_dicts(config, kwargs)
        self._exception = exception

    def __getattr__(self, name):
        if not name.startswith('_'):
            return getattr(self._namespace, name)
        else:
            raise AttributeError(name)

    @property
    def program_help(self):
        return self._parser.format_help().strip()

    # Protected

    _Parser = Parser

    @cachedproperty
    def _namespace(self):
        return self._parser.parse_args(self._argv[1:])

    @cachedproperty
    def _parser(self):
        parser = self._Parser(
            exception=self._exception, **self._parser_config)
        for argument in self._parser_arguments:
            argument = copy(argument)
            try:
                try:
                    args = [argument.pop('name')]
                except KeyError:
                    args = argument.pop('flags')
                parser.add_argument(*args, **argument)
            except:
                raise ValueError(
                    'Bad argparse argument "{argument}"'.
                    format(argument=argument))
        return parser

    @property
    def _parser_arguments(self):
        return self._config.get('arguments', [])

    @property
    def _parser_config(self):
        config = copy(self._config)
        config.pop('arguments', [])
        config.setdefault('prog', os.path.basename(self._argv[0]))
        return config
