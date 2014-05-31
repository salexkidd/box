import sys
import logging
from abc import ABCMeta, abstractmethod
from ..argparse import Program 

class Program(Program, metaclass=ABCMeta):
    
    #Public
     
    def __call__(self):
        self._config()
        self._execute()
         
    #Protected
    
    def _config(self):
        logging.config.dictConfig(self._logging_config)        
        logger = logging.getLogger()
        if self._command.debug:
            logger.setLevel(logging.DEBUG)
        if self._command.verbose:
            logger.setLevel(logging.INFO)
        if self._command.quiet:
            logger.setLevel(logging.ERROR)      
    
    def _execute(self):
        try:
            self._invoke()
        except Exception as exception:
            logging.getLogger(__name__).error(
                self._format_exception(exception), 
                exc_info=self._command.debug)
            sys.exit(1)
            
    @property
    @abstractmethod
    def _logging_config(self):
        pass #pragma: no cover
    
    @abstractmethod    
    def _invoke(self):      
        pass #pragma: no cover
    
    def _format_exception(self, exception):
        return '{category}: {message}'.format(
            category=type(exception).__name__,
            message=str(exception))