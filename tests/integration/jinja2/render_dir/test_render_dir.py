from box.importlib import check_module

if check_module('jinja2'):
    import os
    import shutil
    import jinja2
    import unittest
    from functools import partial
    from unittest.mock import patch
    from box.jinja2 import render_dir


    class render_dir_Test(unittest.TestCase):

        # Public

        def setUp(self):
            os.makedirs(self._make_path('{{ dir }}'), exist_ok=True)
            open(self._make_path('{{ file }}'), 'w').close()
            self.prender = partial(render_dir, jinja2=jinja2)

        def tearDown(self):
            try:
                shutil.rmtree(self._make_path())
            except os.error:
                pass

        def test(self):
            self.prender(self._make_path())
            result = sorted(os.listdir(self._make_path()))
            self.assertEqual(result, ['{{ dir }}', '{{ file }}'])

        def test_with_context(self):
            self.prender(self._make_path(), {'dir': 'dir', 'file': 'file'})
            result = sorted(os.listdir(self._make_path()))
            self.assertEqual(result, ['dir', 'file'])

        @patch('os.rename')
        def test_with_error_in_rendering(self, rename):
            rename.side_effect = Exception()
            self.prender(self._make_path(), {'dir': 'dir', 'file': 'file'})
            result = sorted(os.listdir(self._make_path()))
            self.assertEqual(result, ['{{ dir }}', '{{ file }}'])

        # Protected

        def _make_path(self, *args):
            return os.path.join(os.path.dirname(__file__), 'fixtures', *args)
