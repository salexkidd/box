from box.importlib import check_module

if check_module('sphinx'):
    import sphinx
    import unittest
    from box.sphinx import Settings


    class SettingsTest(unittest.TestCase):

        # Actions

        def setUp(self):
            self.settings = Settings(sphinx=sphinx)

        # Tests

        def test_source_suffix(self):
            self.assertEqual(self.settings.source_suffix, '.rst')
