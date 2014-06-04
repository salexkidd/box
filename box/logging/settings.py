from ..collections import merge_dicts
from ..argparse import Settings

class Settings(Settings):
        
    #Argparse
    
    @property
    def argparse(self):
        super_argparse = getattr(super(Settings, self), 'argpase', {})
        return self._merge_argparse(super_argparse, {
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
        })
    
    #Logging
    
    logging_level = 'WARNING' 
    logging_format = '[%(levelname)s] %(message)s'
    
    @property
    def logging(self):
        super_logging = getattr(super(Settings, self), 'logging', {})        
        return self._merge_logging(super_logging, {
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
        
    #Protected
    
    def _merge_logging(self, logging1, logging2):
        return merge_dicts(logging1, logging2)                   