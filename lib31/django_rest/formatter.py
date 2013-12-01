import json
from abc import ABCMeta, abstractmethod
from lib31.json import DateEncoder

class Formatter(metaclass=ABCMeta):
    
    #Public
    
    @abstractmethod
    def format(self):
        pass #pragma: no cover


class JSONFormatter(Formatter):
    
    #Public
    
    def format(self, struct):
        return json.dumps(struct, cls=DateEncoder)    