import sys
import logging
from abc import ABCMeta, abstractmethod
from ..argparse import Program 
from ..functools import cachedproperty
from .settings import LoggingSettings

class LoggingProgram(Program, metaclass=ABCMeta):
    
    #Public
     
    def __call__(self):
        logging.config.dictConfig(self._logging_config)        
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
            self._argv, config=self._argparse_config)
        
    @abstractmethod    
    def _execute(self):      
        pass #pragma: no cover
              
    @property
    def _argparse_config(self):
        self._settings.argparse
        
    @property
    def _logging_config(self):
        self._settings.logging
           
    @cachedproperty
    def _settings(self):
        return LoggingSettings()       