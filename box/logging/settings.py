from ..packtools import Settings

class LoggingSettings(Settings):
        
    #Console
    
    @property
    def argparse(self):
        argparse = getattr(super(), 'argparse', {})
        argparse.setdefault('arguments', [])
        argparse['arguments'] += [
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
        return argparse
    
    #Logging
    
    logging_level = 'WARNING' 
    logging_format = '[%(levelname)s] %(message)s'
   
    @property
    def logging(self):
        logging = getattr(super(), 'logging', {})
        logging.setdefault('version', 1)
        logging.setdefault('disable_existing_loggers', False)
        logging.setdefault('loggers', {})
        logging.setdefault('handlers', {})
        logging.setdefault('formatters', {})
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
        logging['handlers']['default'] = {
            'format': self.logging_format
        }    
        return logging