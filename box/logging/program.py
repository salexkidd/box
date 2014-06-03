import sys
import logging.config
from abc import ABCMeta, abstractmethod
from ..argparse import Program 
from .settings import Settings

class Program(Program, metaclass=ABCMeta):
    
    #Public
     
    def __call__(self):
        logging.config.dictConfig(self._settings.logging)        
        logger = logging.getLogger()
        if self._command.debug:
            logger.setLevel(logging.DEBUG)
        if self._command.verbose:
            logger.setLevel(logging.INFO)
        if self._command.quiet:
            logger.setLevel(logging.ERROR)
        try:
            self._execute()
        except Exception as exception:
            logging.getLogger(__name__).error(
                str(exception), exc_info=self._command.debug)
            sys.exit(1)            
         
    #Protected
    
    _settings_class = Settings
        
    @abstractmethod    
    def _execute(self):      
        pass #pragma: no cover      