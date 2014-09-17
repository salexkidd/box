import unittest
import datetime
from importlib import import_module
component = import_module('box.json.date')


class DateEncoderTest(unittest.TestCase):

    # Actions

    def setUp(self):
        self.encoder = component.DateEncoder()

    # Tests

    def test_default_with_datetime(self):
        obj = datetime.datetime.today()
        self.assertEqual(self.encoder.default(obj), obj.isoformat())

    def test_default_with_date(self):
        obj = datetime.date.today()
        self.assertEqual(self.encoder.default(obj), obj.isoformat())

    def test_default_with_time(self):
        obj = datetime.time()
        self.assertEqual(self.encoder.default(obj), obj.isoformat())

    def test_default_with_unsupported_type(self):
        obj = datetime
        self.assertRaises(TypeError, self.encoder.default, obj)
