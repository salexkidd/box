from ..packtools import Settings

class LoggingSettings(Settings):
        
    #Argparse
    
    @property
    def argparse(self):
        return {
            'conflict_handler': 'resolve',
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
            ],        
        }
    
    #Logging
    
    logging_level = 'WARNING' 
    logging_format = '[%(levelname)s] %(message)s'
    
    @property
    def logging(self):
        return {
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
        }