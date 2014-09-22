import os
import sys
from copy import copy
from argparse import ArgumentParser
from abc import ABCMeta, abstractmethod


class Program(metaclass=ABCMeta):
    """Abstract console program representation.

    Client have to implement __call__ method.

    Parameters
    ----------
    argv: list
        Program's arguments like sys.argv.
    config: dict
        Argparse configuration.
    exception: :class:`Exception`
        Exception class to raise instead of exit.

    Examples
    --------
    Usage exmaple::

      >>> from box.argparse import Program
      >>> class Program(Program):
      ...   def __call__(self):
      ...     print(self._command.arguments)
      >>> config = {'arguments': [{'name': 'arguments', 'nargs':'*'}]
      >>> program = Program(['program', 'arg'], config=config)
      >>> program()
      ['arg']
    """

    # Public

    default_argv = sys.argv
    default_config = {}

    def __init__(self, argv=None, *,
                 config=None, parser=None, exception=None):
        if argv is None:
            argv = self.default_argv
        if config is None:
            config = self.default_config
        self.__argv = argv
        self.__config = config
        self.__exception = exception

    def __getattr__(self, name):
        return getattr(self.__namespace, name)

    @abstractmethod
    def __call__(self):
        pass  # pragma: no cover

    # Private

    # TODO: add cachedproperty
    @property
    def __namespace(self):
        try:
            return self.__parser.parse_args(self.__argv[1:])
        except SystemExit:
            raise self.__exception()

    # TODO: add cachedproperty
    @property
    def __parser(self):
        config = copy(self.__config)
        arguments = config.pop('arguments', [])
        config.setdefault('prog', os.path.basename(self.__argv[0]))
        parser = ArgumentParser(**config)
        for argument in arguments:
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
