import datetime
from json import JSONEncoder

class DateEncoder(JSONEncoder):
    
    #Public
    
    def default(self, obj):
        if isinstance(obj, self.date_types):
            return obj.isoformat()
        return super(DateEncoder, self).default(obj)
    
    date_types = (
        datetime.datetime, 
        datetime.date, 
        datetime.time,
    )