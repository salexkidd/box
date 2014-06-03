from ..packtools import Settings

class Settings(Settings):

    #Argparse
    
    @property
    def argparse(self):
        argparse = getattr(super(), 'argparse', {})
        argparse.setdefault('arguments', [])
        argparse['arguments'].extend([
            {
             'name': 'arguments',
             'nargs':'*',
            },
        ])
        return argparse