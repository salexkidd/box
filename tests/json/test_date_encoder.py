import unittest
from lib31.json.date_encoder import DateEncoder

class DateEncoderTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.encoder = DateEncoder()