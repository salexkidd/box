box.packtools
=============

Module provides two classes for better settings and version managment.
They could be used for different purposes but the most obvious way to use it is
as package settings and version. That's how box uses it for itself.

Public
------

Module’s public interface.

.. autoclass:: box.packtools.Settings
     :members: _extensions
 
.. autoclass:: box.packtools.Version

Internal
--------

Module’s internal implementation.
     
.. autoclass:: box.packtools.settings.SettingsMetaclass