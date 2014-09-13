from .object import import_object


def inject(name, *, module=None, package=None):
    """Return imported object wrapped in property.

    Examples
    --------
    When you can't import object explicitly it injects object
    as property using "lazy load" principle::

      class Client:
          patch = inject('unittest.mock.patch')

    It's basicly equal to::

      class Client:
          @property
          def patch(self):
              return import_object('unittest.mock.patch')

    .. seealso:: :func:`box.importlib.import_object`
    """
    return property(
        lambda self: import_object(name, module=module, package=package))
