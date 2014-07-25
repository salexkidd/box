=============
box.functools
=============

Module adds some functionality to standard functools module.

------
Public
------

Module’s public interface.

.. class:: box.functools.cachedproperty
     
     Property with caching.

.. autoclass:: box.functools.Function
.. autoclass:: box.functools.Decorator
.. autoclass:: box.functools.Null    

--------
Internal
--------

Module's internal implementation.

.. autoclass:: box.functools.function.FunctionMetaclass
.. autoclass:: box.functools.decorator.DecoratorMetaclass
.. autoclass:: box.functools.null.NullMetaclass