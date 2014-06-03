from ..packtools import Settings

class Settings(Settings):

    #Public
    
    @property
    def argparse(self):
        return {
            'arguments': [
                {
                 'name': 'arguments',
                 'nargs':'*',
                },
            ],       
        }