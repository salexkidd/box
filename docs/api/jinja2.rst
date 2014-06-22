==========
box.jinja2
==========

Module extends popular templating package jinja2.

.. warning:: Jinja2 is not in box dependencies list. You have
     to install it to use this module.

------
Public
------

Module’s public interface.
     
Functions to work with jinja2 using one line of code.
They support object as context (lazy name/attribute instead of key/value).

.. autoclass:: box.jinja2.render_string
.. autoclass:: box.jinja2.render_file
.. autoclass:: box.jinja2.render_dir

--------
Internal
--------

Module’s internal implementation.

.. autoclass:: box.jinja2.context.ObjectContext 