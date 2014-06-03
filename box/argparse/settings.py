import operator
from ..collections import merge_dicts
from ..packtools import Settings

class Settings(Settings):

    #Argparse
    
    @property
    def argparse(self):
        return self._derive_argparse({
            'arguments': [
                {
                 'name': 'arguments',
                 'nargs':'*',
                },
            ]
        })
        
    #Protected
    
    def _derive_argparse(self, argparse):
        return merge_dicts(getattr(super(), 'argparse', {}), argparse, 
                           resolvers={list: operator.add})
        