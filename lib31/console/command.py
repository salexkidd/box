from copy import deepcopy
from argparse import ArgumentParser
from ..python.cachedproperty import cachedproperty

class Command:
    
    #Public
    
    def __init__(self, argv, schema):
        self.argv = argv        
        self.schema = schema
        
    def __getattr__(self, name):
        if not name.startswith('_'):
            return getattr(self._parsed_args, name)
        else:
            raise AttributeError(name)
        
    #Protected
    
    _parser_class = ArgumentParser

    @cachedproperty
    def _parsed_args(self):
        return self._parser.parse_args(self.argv[1:])
        
    @cachedproperty
    def _parser(self):
        #TODO: fix config work
        parser = self._parser_class(self.schema['config'])
        for name, data in deepcopy(self.schema['arguments']).items():
            parser.add_argument(name, **data)
        for name, data in deepcopy(self.schema['options']).items():
            parser.add_argument(*data.pop('flags'), dest=name, **data)
        return parser