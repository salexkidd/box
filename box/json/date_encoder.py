import datetime
from json import JSONEncoder

class DateEncoder(JSONEncoder):
    """Json encoder with support of datatime values.

    If encoder meets datetime.datetime, datetime.date or datetime.time
    in python objects to dump it will be encoded by **isoformat** method::

      >>> import json
      >>> import datetime
      >>> from box.json import DateEncoder
      >>> date = datetime.date(1970,1,1)
      >>> json.dumps({'date': date}, cls=DateEncoder)
      '{"date": "1970-01-01"}'
    """

    # Public

    def default(self, obj):
        if isinstance(obj, self._date_types):
            return obj.isoformat()
        else:
            return super().default(obj)

    # Protected

    _date_types = (
        datetime.datetime,
        datetime.date,
        datetime.time,
    )
