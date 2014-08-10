=============
box.findtools
=============

Module provides finding functionality based on map_reduce concept
and python generators. 

------
Public
------

Module’s public interface.

Finders
-------

.. autoclass:: box.findtools.find
.. autoclass:: box.findtools.find_files
.. autoclass:: box.findtools.find_strings
.. autoclass:: box.findtools.find_objects

Emitters
--------

.. autoclass:: box.findtools.Emitter
.. autoclass:: box.findtools.FileEmitter
.. autoclass:: box.findtools.StringEmitter
.. autoclass:: box.findtools.ObjectEmitter

Constraints
-----------

.. autoclass:: box.findtools.Constraint
.. autoclass:: box.findtools.CompositeConstraint
.. autoclass:: box.findtools.PatternConstraint

Exceptions
----------

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