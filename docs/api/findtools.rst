=============
box.findtools
=============

Module provides finding functionality based on map_reduce concept
and python generators. 

------
Public
------

Module’s public interface.

There are three main functions to find files, strings and python objects.

.. autoclass:: box.findtools.find_files
.. autoclass:: box.findtools.FindFilesEmitter

.. autoclass:: box.findtools.find_strings
.. autoclass:: box.findtools.FindStringsEmitter

.. autoclass:: box.findtools.find_objects
.. autoclass:: box.findtools.FindObjectsEmitter

.. autoclass:: box.findtools.NotFound

--------
Internal
--------

Module’s internal implementation.

.. autoclass:: box.findtools.filename.FilenameMapper
.. autoclass:: box.findtools.filepath.FilepathMapper
.. autoclass:: box.findtools.maxdepth.MaxdepthMapper
.. autoclass:: box.findtools.objname.ObjnameMapper
.. autoclass:: box.findtools.objtype.ObjtypeMapper