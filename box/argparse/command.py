from copy import copy
from argparse import ArgumentParser
from box.functools import cachedproperty

class Command:
    
    #Public
    
    default_config = {
        'prog': 'program',
        'add_help': True,                     
        'arguments': [
            {
             'name': 'arguments',
             'nargs':'*',
            },             
        ],       
    }
    
    def __init__(self, argv, config=None, **kwargs):
        self._argv = argv
        self._config = config
        if self._config == None: 
            self._config = copy(self.default_config)
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
        arguments = self._config.get('arguments', [])
        return arguments    
    
    @property
    def _parser_config(self):
        config = copy(self._config)
        config.pop('arguments', [])
        return config
            
    
class SilentArgumentParser(ArgumentParser):
    
    #Public
    
    def error(self, message):
        raise SilentArgumentParserException(message)
    
    
class SilentArgumentParserException(Exception): pass    