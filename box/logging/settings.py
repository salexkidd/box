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
                 'dest': 'debug',
                 'action': 'store_true',
                 'flags': ['-d', '--debug'],
                 'help': 'Enable debug mode.',
                },
                {
                 'dest': 'quiet',
                 'action': 'store_true',
                 'flags': ['-q', '--quiet'],
                 'help': 'Enable quiet mode.',
                }, 
                {
                 'dest': 'verbose',
                 'action': 'store_true',
                 'flags': ['-v', '--verbose'],
                 'help': 'Enable verbose mode.',                 
                },  
            ]
        }, resolvers={list: operator.add})
    
    #Logging
    
    logging_level = 'WARNING' 
    logging_format = '[%(levelname)s] %(message)s'
    
    @property
    def logging(self):
        return merge_dicts(getattr(super(), 'logging', {}), {
            'version': 1,
            'disable_existing_loggers': False,
            'loggers': {
                '': {
                    'handlers': ['default'],        
                    'level': self.logging_level,
                    'propagate': True,
                },                                   
            },
            'handlers': {
                'default': {
                    'level':'DEBUG',    
                    'class':'logging.StreamHandler',
                    'formatter': 'default',
                },                                                   
            },
            'formatters': {
                'default': {
                    'format': self.logging_format
                },                                                
            },
        })             