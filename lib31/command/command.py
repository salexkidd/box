from copy import deepcopy
from argparse import ArgumentParser
from ..cachedproperty import cachedproperty

class Command(object):
    
    #Public
    
    argv = []
    schema = {
        'config': {
            'prog': 'name',
            'add_help': False,
        },                      
        'arguments': {
            'argument': {
                'nargs':'?',
            },
        },
        'options': {},
    }
    parser = ArgumentParser
    
    def __init__(self, argv, schema=None, parser=None):
        self.argv = argv        
        self.schema = schema or self.schema
        self.parser = parser or self.parser
        self.parse()
        
    def __getattr__(self, name):
        return getattr(self._parsed, name)
        
    #Protected

    def _parse(self):
        self._parsed = self._parser.parse_args(self.argv[1:])
        
    @cachedproperty
    def _parser(self):
        parser = self.parser(self.schema['config'])
        for name, data in deepcopy(self.schema['arguments']).items():
            parser.add_argument(name, **data)
        for name, data in deepcopy(self.schema['options']).items():
            parser.add_argument(*data.pop('flags'), dest=name, **data)
        return parser
