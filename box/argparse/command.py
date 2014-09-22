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
        self.__argv = argv
        self.__config = merge_dicts(config, kwargs)
        self.__exception = exception

    def __getattr__(self, name):
        if not name.startswith('_'):
            return getattr(self._namespace, name)
        else:
            raise AttributeError(name)

    @property
    def program_help(self):
        return self.__parser.format_help().strip()

    # Protected

    _Parser = Parser

    @cachedproperty
    def _namespace(self):
        return self.__parser.parse_args(self.__argv[1:])

    # Private

    # TODO: add cachedproperty
    @cachedproperty
    def __parser(self):
        parser = self._Parser(
            exception=self.__exception, **self.__parser_config)
        for argument in self.__parser_arguments:
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
    def __parser_arguments(self):
        return self.__config.get('arguments', [])

    @property
    def __parser_config(self):
        config = copy(self.__config)
        config.pop('arguments', [])
        config.setdefault('prog', os.path.basename(self.__argv[0]))
        return config
