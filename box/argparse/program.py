import os
import sys
from copy import copy
from argparse import ArgumentParser
from abc import ABCMeta, abstractmethod
from ..functools import Function


class Program(Function, metaclass=ABCMeta):
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
      >>> class program(Program):
      ...   def __call__(self):
      ...     print(self.arguments)
      >>> config = {'arguments': [{'name': 'arguments', 'nargs':'*'}]
      >>> program(['program', 'arg'], config=config)
      ['arg']
    """

    # Public

    default_config = {}

    def __init__(self, argv=None, *, config=None, exception=None):
        if argv is None:
            argv = sys.argv
        if config is None:
            config = self.default_config
        self.__argv = argv
        self.__config = config
        self.__exception = exception

    def __getitem__(self, key):
        try:
            return getattr(self.__namespace, key)
        except AttributeError:
            raise KeyError(key) from None

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name) from None

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
            if self.__exception is not None:
                raise self.__exception()
            raise

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
