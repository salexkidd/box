from copy import deepcopy
from lib31.decorators.cachedproperty import cachedproperty
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
            'arguments': {
                'nargs':'*',
                'default': [],
            },
        },
        'options': {},
    }
    
    def __init__(self, argv, schema=None):
        self.argv = argv        
        self.schema = schema or self.schema
        
    def __getattr__(self, name):
        return getattr(self._parsed, name)
        
    #Protected
    
    _parser_class = CommandArgumentParser

    @cachedproperty
    def _parsed(self):
        return self._parser.parse_args(self.argv[1:])
        
    @cachedproperty
    def _parser(self):
        parser = self._parser_class(self.schema['config'])
        for name, data in deepcopy(self.schema['arguments']).items():
            parser.add_argument(name, **data)
        for name, data in deepcopy(self.schema['options']).items():
            parser.add_option(*data.pop('flags'), dest=name, **data)
        return parser
