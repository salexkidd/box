import datetime
from json import JSONEncoder

class DateEncoder(JSONEncoder):
    
    #Public
    
    def default(self, obj):
        if isinstance(obj, self._date_types):
            return obj.isoformat()
        return super().default(obj)
    
    #Protected
    
    _date_types = (
        datetime.datetime, 
        datetime.date, 
        datetime.time,
    )