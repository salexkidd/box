import unittest
from box.string.canvas import Canvas


class CanvasStringTest(unittest.TestCase):

    # Public

    def test(self):
        canvas = Canvas(text='test "{hex}"', hex='{dec:x}', dec=15)
        self.assertEqual(canvas.text, 'test "f"')
