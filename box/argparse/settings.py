import operator
from functools import partial
from ..collections import merge_dicts
from ..packtools import Settings

class Settings(Settings):

    #Argparse
    
    @property
    def argparse(self):
        pmerge_dicts = partial(merge_dicts, resolvers={list: operator.add})
        return pmerge_dicts(getattr(super(), 'argparse', {}), {
            'arguments': [
                {
                 'name': 'arguments',
                 'nargs':'*',
                },
            ]
        })