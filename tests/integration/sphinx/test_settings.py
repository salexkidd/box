from box.importlib import check_module

if check_module('sphinx'):
    import unittest
    from box.sphinx import Settings


    class SettingsTest(unittest.TestCase):

        # Public

        def setUp(self):
            self.settings = Settings()

        def test_source_suffix(self):
            self.assertEqual(self.settings.source_suffix, '.rst')
