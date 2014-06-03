import operator
from ..collections import merge_dicts
from ..packtools import Settings

class Settings(Settings):

    #Argparse
    
    @property
    def argparse(self):
        argparse1 = getattr(super(), 'argparse', {})
        argparse2 = {
            'arguments': [
                {
                 'name': 'arguments',
                 'nargs':'*',
                },
            ]
        }
        return merge_dicts(argparse1, argparse2, 
            resolvers={list: operator.add})