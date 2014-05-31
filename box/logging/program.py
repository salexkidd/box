import sys
import logging.config
from abc import ABCMeta, abstractmethod
from ..argparse import Program 
from ..functools import cachedproperty
from .settings import LoggingSettings

class LoggingProgram(Program, metaclass=ABCMeta):
    
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
    
    @cachedproperty
    def _command(self):
        return self._command_class(
            self._argv, config=self._settings.argparse)
        
    @abstractmethod    
    def _execute(self):      
        pass #pragma: no cover
         
    @cachedproperty
    def _settings(self):
        return LoggingSettings()       