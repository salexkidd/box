import os
import box
import sphinx
from packgram.sphinx import Settings


class Settings(Settings):

    # Documentation:
    # http://sphinx-doc.org/config.html

    # Project

    project = 'box'
    author = 'roll'
    copyright = '2014, Respect31'
    version = box.version

    # Autodoc

    autodoc_member_order = 'bysource'
    autodoc_default_flags = ['members', 'special-members']
    autodoc_skip_members = ['__weakref__']


locals().update(Settings(sphinx=sphinx))
