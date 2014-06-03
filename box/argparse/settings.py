import operator
from ..collections import merge_dicts
from ..packtools import Settings

class Settings(Settings):

    #Argparse
    
    @property
    def argparse(self):
        return merge_dicts(getattr(super(), 'argparse', {}), {
            'arguments': [
                {
                 'name': 'arguments',
                 'nargs':'*',
                },
            ]
        }, resolvers={list: operator.add})