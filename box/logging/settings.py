from ..packtools import Settings

class Settings(Settings):
        
    #Argparse
    
    @property
    def argparse(self):
        argparse = getattr(super(), 'argparse', {})
        argparse.setdefault('arguments', [])
        argparse['arguments'].extend([
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
        ])
        return argparse
    
    #Logging
    
    logging_level = 'WARNING' 
    logging_format = '[%(levelname)s] %(message)s'
    
    @property
    def logging(self):
        logging = getattr(super(), 'logging', {})
        logging.setdefault('loggers', {})
        logging.setdefault('handlers', {})
        logging.setdefault('formatters', {})        
        logging['version'] = 1
        logging['disable_existing_loggers'] = False
        logging['loggers'][''] = {
            'handlers': ['default'],        
            'level': self.logging_level,
            'propagate': True,
        }
        logging['handlers']['default'] = {
            'level':'DEBUG',    
            'class':'logging.StreamHandler',
            'formatter': 'default',
        }
        logging['formatters']['default'] = {
            'format': self.logging_format
        }    
        return logging        