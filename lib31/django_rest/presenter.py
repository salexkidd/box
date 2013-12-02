from abc import ABCMeta, abstractmethod
from .builder import JSONBuilder
from .exceptions import FormatIsNotSuppported

class Presenter(metaclass=ABCMeta):
    
    #Public
    
    def __init__(self, response):
        self._response = response
        
    @abstractmethod
    def format(self):
        pass #pragma: no cover
    
    #Protected
    
    @property
    def _response_dict(self):
        return {'result': self._response.result,
                'error': self._response.error}
    

class MappingPresenter(Presenter):

    #Public

    def format(self):
        raise FormatIsNotSuppported()

    #Protected
    _parser_classes = {}
    _parser_packages = []
    _builder_classes = {'json': JSONBuilder}
    _builder_packages = []
    