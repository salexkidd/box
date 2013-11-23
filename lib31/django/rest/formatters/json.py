json = __import__('json', level=0)
from lib31.json import DateEncoder
from ..formatter import RestFormatter

class JSON(RestFormatter):
    
    #Public
    
    def process(self, struct):
        return json.dumps(struct, cls=DateEncoder)