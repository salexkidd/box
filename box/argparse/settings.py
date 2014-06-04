import operator
from ..collections import merge_dicts
from ..packtools import Settings

class Settings(Settings):
        
    #Protected
    
    def _merge_argparse(self, argparse1, argparse2):
        return merge_dicts(argparse1, argparse2, 
                           resolvers={list: operator.add})
        