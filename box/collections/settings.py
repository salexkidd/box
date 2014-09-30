from .include import include


class Settings(dict):
    """Settings representation.

    Parameters
    ----------
    settings: dict
        Dict to override settings values.
    kwargs: dict
        Key=value pairs to override settings values.

    Examples
    --------
    Usage example::

      >>> from box.package import Settings
      >>> class Settings(Settings):
      ...   attr1 = 'value1'
      ...   attr2 = 'value2'
      ...
      >>> s = Settings(attr1='new1')
      >>> s
      {'attr1': 'new1', 'attr2': 'value2'}
    """

    # Public

    def __init__(self, **kwargs):
        vars(self).update(kwargs)
        self.update(self.__as_dict)

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        self.update(self.__as_dict)

    def __delattr__(self, name):
        super().__delattr__(name)
        self.clear()
        self.update(self.__as_dict)

    # Private

    @property
    def __as_dict(self):
        items = {}
        for name in dir(self):
            if not name.startswith('_'):
                attr = getattr(self, name)
                if callable(attr):
                    if not getattr(attr, include.marker, False):
                        # Callable doesn't use @include decorator - skip
                        continue
                items[name] = attr
        return items
