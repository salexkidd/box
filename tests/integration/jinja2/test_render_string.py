from box.importlib import check_module

if check_module('jinja2'):
    import unittest
    from box.jinja2 import render_string
    
    class render_string_Test(unittest.TestCase):
    
        #Public
    
        def test(self):
            pass