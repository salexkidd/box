from copy import deepcopy
from ..cachedproperty import cachedproperty
from .parser import CommandArgumentParser

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
    
    def __init__(self, argv, schema=None):
        self.argv = argv        
        self.schema = schema or self.schema
        self.parse()
        
    def __getattr__(self, name):
        return getattr(self._parsed, name)
        
    #Protected
    
    _parser_class = CommandArgumentParser

    def _parse(self):
        self._parsed = self._parser.parse_args(self.argv[1:])
        
    @cachedproperty
    def _parser(self):
        parser = self._parser_class(self.schema['config'])
        for name, data in deepcopy(self.schema['arguments']).items():
            parser.add_argument(name, **data)
        for name, data in deepcopy(self.schema['options']).items():
            parser.add_argument(*data.pop('flags'), dest=name, **data)
        return parser
