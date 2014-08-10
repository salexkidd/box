=============
box.findtools
=============

Module provides finding functionality based on map_reduce concept
and python generators. 

------
Public
------

Module’s public interface.

There are base and three main functions to find files, 
strings and python objects.

.. autoclass:: box.findtools.find
.. autoclass:: box.findtools.find_files
.. autoclass:: box.findtools.find_strings
.. autoclass:: box.findtools.find_objects

Corresponding emitters:

.. autoclass:: box.findtools.Emitter
.. autoclass:: box.findtools.FileEmitter
.. autoclass:: box.findtools.StringEmitter
.. autoclass:: box.findtools.ObjectEmitter

Base constraints:

.. autoclass:: box.findtools.Constraint
.. autoclass:: box.findtools.CompositeConstraint
.. autoclass:: box.findtools.PatternConstraint

Not emitted exception:

.. autoclass:: box.findtools.NotFound

--------
Internal
--------

Module’s internal implementation.

.. autoclass:: box.findtools.filename.FilenameConstraint
.. autoclass:: box.findtools.filepath.FilepathConstraint
.. autoclass:: box.findtools.maxdepth.MaxdepthConstraint
.. autoclass:: box.findtools.objname.ObjnameConstraint
.. autoclass:: box.findtools.objtype.ObjtypeConstraint