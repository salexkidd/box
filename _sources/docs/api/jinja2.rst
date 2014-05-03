box.jinja2
==========

Module extends popular templating package jinja2.

.. warning:: Jinja2 is not in box dependencies list. You have
     to install it to use this module.

Main
----
     
Functions to work with jinja2 using one line of code.
They support object as context (lazy name/attribute instead of key/value).

.. autoclass:: box.jinja2.render_string
.. autoclass:: box.jinja2.render_file
.. autoclass:: box.jinja2.render_dir

Advanced
--------

Module provides additional elements.

.. automodule:: box.jinja2
     :members:
     :imported-members:
     :exclude-members: render_string, render_file, render_dir 