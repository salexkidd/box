import json
from abc import ABCMeta, abstractmethod
from lib31.json import DateEncoder

class Builder(metaclass=ABCMeta):
    
    @abstractmethod
    def build(self, response):
        pass #pragma: no cover
        

class JSONBuilder(Builder):
    
    #Public
    
    def format(self):
        return json.dumps(self._response_dict, cls=DateEncoder)