from abc import ABCMeta, abstractmethod
from .exceptions import ConstraintsAreNotSuppported

class Parser(metaclass=ABCMeta):
    
    @abstractmethod
    def parse(self, http_request, url_request):
        pass #pragma: no cover
        

class DefaultParser(Parser):
    
    #Public
    
    def parse(self, http_request, url_request):
        result = {}
        if constraints:
            groups = constraints.split(';')
            for group in groups:
                try:
                    name, value = group.split('=')
                    result[name] = self._process_value(name, value)
                except ValueError:
                    raise ConstraintsAreNotSuppported(constraints)
        return result
    
    #Protected
    
    _pattern = '(?P<version>[^/]*)/(?P<format>[^/]*)/(?P<resource>[^/]*)(?:/(?P<constraints>[^/]*))?'
 
    #TODO: compare with run program logic
    @staticmethod   
    def _process_value(name, value):
        try:
            if not value:
                raise Exception() 
            if name in []:
                return str(value)
            else:
                return int(value)
        except Exception:
            raise ValueError()