========
box.find
========

Module provides finding functionality based on map_reduce concept
and python generators. 

------
Public
------

Module’s public interface.

Finders
-------

.. autoclass:: box.find.find
.. autoclass:: box.find.find_files
.. autoclass:: box.find.find_strings
.. autoclass:: box.find.find_objects

Emitters
--------

.. autoclass:: box.find.Emitter
.. autoclass:: box.find.FileEmitter
.. autoclass:: box.find.StringEmitter
.. autoclass:: box.find.ObjectEmitter

Constraints
-----------

.. autoclass:: box.find.Constraint
.. autoclass:: box.find.CompositeConstraint
.. autoclass:: box.find.PatternConstraint

Exceptions
----------

.. autoclass:: box.find.NotFound

--------
Internal
--------

Module’s internal implementation.

.. autoclass:: box.find.filename.FilenameConstraint
.. autoclass:: box.find.filepath.FilepathConstraint
.. autoclass:: box.find.maxdepth.MaxdepthConstraint
.. autoclass:: box.find.objname.ObjnameConstraint
.. autoclass:: box.find.objtype.ObjtypeConstraint