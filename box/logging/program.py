import sys
import logging
from abc import ABCMeta, abstractmethod
from ..argparse import Program 

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
            
    @property
    @abstractmethod
    def _logging_config(self):
        pass #pragma: no cover
    
    @abstractmethod    
    def _execute(self):      
        pass #pragma: no cover