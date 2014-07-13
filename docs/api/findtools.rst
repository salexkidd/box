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

.. autoclass:: box.findtools.constraint.Constraint
.. autoclass:: box.findtools.constraint.CompositeConstraint
.. autoclass:: box.findtools.constraint.PatternConstraint
.. autoclass:: box.findtools.filename.FilenameConstraint
.. autoclass:: box.findtools.filepath.FilepathConstraint
.. autoclass:: box.findtools.maxdepth.MaxdepthConstraint
.. autoclass:: box.findtools.objname.ObjnameConstraint
.. autoclass:: box.findtools.objtype.ObjtypeConstraint