=============
box.packaging
=============

Module provides two classes for better settings and version managment.
They could be used for different purposes but the most obvious way to use it is
as package settings and version. That's how box uses it for itself.

------
Public
------

Module’s public interface.

.. autoclass:: box.packaging.Settings
     :members: _extensions
 
.. autoclass:: box.packaging.Version
.. autoclass:: box.packaging.include

--------
Internal
--------

Module’s internal implementation.
     
.. autoclass:: box.packaging.settings.SettingsMetaclass