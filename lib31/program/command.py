from copy import deepcopy
from argparse import ArgumentParser
from lib31.python import cachedproperty

class Command:
    
    #Public
    
    argparse = {
        'prog': 'program',
        'add_help': True,                     
        'arguments': [
            {
             'name': 'arguments',
             'nargs':'*',
            },             
        ],       
    }
    
    def __init__(self, argv, argparse=None):
        self.argv = argv        
        self.argparse = argparse or self.argparse
        
    def __getattr__(self, name):
        if not name.startswith('_'):
            return getattr(self._namespace, name)
        else:
            raise AttributeError(name)
        
    @cachedproperty    
    def program_help(self):
        return self._parser.format_help().strip()
        
    #Protected
    
    _parser_class = ArgumentParser

    @cachedproperty
    def _namespace(self):
        return self._parser.parse_args(self.argv[1:])
       
    @cachedproperty
    def _parser(self):
        argparse = deepcopy(self.argparse)
        arguments = argparse.pop('arguments')
        parser = self._parser_class(**argparse)
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
                    'Name or flags is required in argparse argument')
        return parser
    
    
class SilentArgumentParser(ArgumentParser):
    
    #Public
    
    def error(self, message):
        raise SilentArgumentParserException(message)
    
    
class SilentArgumentParserException(Exception):
    
    #Public
    
    pass    