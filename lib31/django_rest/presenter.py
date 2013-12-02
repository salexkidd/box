from abc import ABCMeta, abstractmethod
from .builder import JSONBuilder
from .parser import DefaultParser
from .exceptions import FormatIsNotSuppported, VersionIsNotSuppported

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

    def parse(self, http_request, url_request):
        pass #pragma: no cover
    
    def build(self, response):
        pass #pragma: no cover

    #Protected
    _parser_classes = {'*': DefaultParser}
    _parser_packages = []
    _builder_classes = {'json': JSONBuilder}
    _builder_packages = []
    