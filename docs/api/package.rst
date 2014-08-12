===========
box.package
===========

Module provides two classes for better settings and version managment.
They could be used for different purposes but the most obvious way to use it is
as package settings and version. That's how box uses it for itself.

------
Public
------

Module’s public interface.

.. autoclass:: box.package.Settings
     :members: _extensions
 
.. autoclass:: box.package.Version
.. autoclass:: box.package.include

--------
Internal
--------

Module’s internal implementation.
     
.. autoclass:: box.package.settings.SettingsMetaclass