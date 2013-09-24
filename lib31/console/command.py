from copy import deepcopy
from argparse import ArgumentParser

class Command:
    
    #Public
    
    schema = {
        'prog': 'program',
        'add_help': False,                     
        'arguments': [
            {
             'name': 'arguments',
             'nargs':'*',
            },             
        ],       
    }
    
    def __init__(self, argv, schema=None):
        self.argv = argv        
        self.schema = schema or self.schema
        
    def __getattr__(self, name):
        if not name.startswith('_'):
            return getattr(self._namespace, name)
        else:
            raise AttributeError(name)
        
    #Protected
    
    _parser_class = ArgumentParser

    #TODO: use cachedproperty
    @property
    def _namespace(self):
        return self._parser.parse_args(self.argv[1:])
       
    #TODO: use cachedproperty        
    @property
    def _parser(self):
        schema = deepcopy(self.schema)
        arguments = schema.pop('arguments')
        parser = self._parser_class(**schema)
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
                raise ValueError('Name or flags is required in command_schema argument')
        return parser