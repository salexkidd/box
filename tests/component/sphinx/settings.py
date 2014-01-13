import unittest
from box.sphinx.settings import Settings

class SettingsTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.settings = Settings()
        
    def test__default(self):
        self.assertEqual(self.settings.html_theme, 'default')