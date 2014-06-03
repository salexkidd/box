class Settings:

    #Public
    
    @property
    def argparse(self):
        return {
            'add_help': True,                     
            'arguments': [
                {
                 'name': 'arguments',
                 'nargs':'*',
                },
            ],       
        }