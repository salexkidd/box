import os
from copy import copy
from argparse import ArgumentParser
from ..functools import cachedproperty

class Command:
    """Console command representation.
    
    :param list argv: program's arguments like sys.argv
    :param dict config: command configuration for argparse
    :param dict kwargs: key=value command configuration pairs
    
    Command provides access to command line arguments by attribute names:
    
    >>> from box.argparse import Command
    >>> config = {'arguments': [{'name': 'arguments', 'nargs':'*'}]}    
    >>> command = Command(['program', 'arg'], config=config)
    >>> command.arguments
    ['arg']
    """
    
    #Public
    
    def __init__(self, argv, config, **kwargs):
        self._argv = argv
        self._config = copy(config)
        self._config.update(kwargs)
        
    def __getattr__(self, name):
        if not name.startswith('_'):
            return getattr(self._namespace, name)
        else:
            raise AttributeError(name)
        
    @property    
    def program_help(self):
        return self._parser.format_help().strip()
        
    #Protected
    
    _parser_class = ArgumentParser

    @cachedproperty
    def _namespace(self):
        return self._parser.parse_args(self._argv[1:])
       
    @cachedproperty
    def _parser(self):
        parser = self._parser_class(**self._parser_config)
        for argument in self._parser_arguments:
            argument = copy(argument)
            try:
                try:
                    args = [argument.pop('name'),]
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
            
    
class SilentArgumentParser(ArgumentParser):
    """Argument parser with raising exception instead of program exit.
    """
    
    #Public
    
    def error(self, message):
        raise SilentArgumentParserException(message)
    
    
class SilentArgumentParserException(Exception): pass