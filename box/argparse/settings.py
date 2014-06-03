from ..packtools import Settings

class Settings(Settings):

    #Public
    
    @property
    def argparse(self):
        return {
            'conflict_handler': 'resolve',                
            'arguments': [
                {
                 'name': 'arguments',
                 'nargs':'*',
                },
            ],       
        }