import unittest
from box.findtools.not_found import NotFound

class NotFoundTest(unittest.TestCase):

    # Public

    def test(self):
        self.assertRaises(NotFound, self._raise)

    # Protected

    def _raise(self):
        raise NotFound()
