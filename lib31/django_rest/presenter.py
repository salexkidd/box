from abc import ABCMeta, abstractmethod
from .builder import JSONBuilder
from .exceptions import FormatIsNotSuppported

class Presenter(metaclass=ABCMeta):
    
    #Public
    
    @abstractmethod
    def parse(self, http_request, url_request):
        pass #pragma: no cover
    
    @abstractmethod
    def build(self, response):
        pass #pragma: no cover
    

class MappingPresenter(Presenter):

    #Public

    @abstractmethod
    def parse(self, http_request, url_request):
        pass #pragma: no cover
    
    @abstractmethod
    def build(self, response):
        pass #pragma: no cover

    #Protected
    _parser_classes = {}
    _parser_packages = []
    _builder_classes = {'json': JSONBuilder}
    _builder_packages = []
    