from copy import deepcopy
from argparse import ArgumentParser
from lib31.python import cachedproperty

class Command:
    
    #Public
    
    #TODO: use names like initial_config and move main to property
    def __init__(self, argv, config=None):
        self._argv = argv        
        self._config = config or self._default_config
        
    def __getattr__(self, name):
        if not name.startswith('_'):
            return getattr(self._namespace, name)
        else:
            raise AttributeError(name)
        
    @cachedproperty    
    def program_help(self):
        return self._parser.format_help().strip()
        
    #Protected
    
    _default_config = {
        'prog': 'program',
        'add_help': True,                     
        'arguments': [
            {
             'name': 'arguments',
             'nargs':'*',
            },             
        ],       
    }
    _parser_class = ArgumentParser

    @cachedproperty
    def _namespace(self):
        return self._parser.parse_args(self._argv[1:])
       
    @cachedproperty
    def _parser(self):
        config = deepcopy(self._config)
        arguments = config.pop('arguments')
        parser = self._parser_class(**config)
        for argument in arguments:
            #Positional argument
            if 'name' in argument:
                name = argument.pop('name')
                parser.add_argument(name, **argument)
            #Optional argument
            elif 'flags' in argument:
                flags = argument.pop('flags')
                parser.add_argument(*flags, **argument)
            #Unknown argument
            else:
                raise ValueError(
                    'Bad argparse argument "{argument}"'.
                    format(argument=argument))
        return parser
    
    
class SilentArgumentParser(ArgumentParser):
    
    #Public
    
    def error(self, message):
        raise SilentArgumentParserException(message)
    
    
class SilentArgumentParserException(Exception): pass    