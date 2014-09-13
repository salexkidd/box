from collections import OrderedDict
from ..collections import merge_dicts


class Version(str):
    """Version representation.

    Parameters
    ----------
    kwargs: dict
        Key=value pairs to override version elements.

    Examples
    --------
    Usage example::

      >>> from box.package import Version
      >>> class Version(Version):
      ...   major = 1
      ...   minor = 2
      ...   micro = 3
      ...
      >>> v = Version(micro=5)
      >>> v
      '1.2.5'
      >>> v.major
      1
      >>> v.info
      (1, 2, 5, 'final', 0)

    .. seealso:: Python versioning: sys.version_info
    """

    # Public

    major = 0
    """Version's major component.
    """
    minor = 0
    """Version's minor component.
    """
    micro = 0
    """Version's micro component.
    """
    level = 'final'
    """Version's level.
    """
    serial = 0
    """Version's serial.
    """

    def __new__(cls, version=None, **kwargs):
        ekwargs = kwargs
        if version is not None:
            ekwargs = merge_dicts(version.__as_dict, kwargs)
        # Buffer version
        version = str.__new__(cls)
        vars(version).update(ekwargs)
        # Actual version
        version = str.__new__(cls, version.__as_str)
        vars(version).update(ekwargs)
        return version

    @property
    def info(self):
        """Version as a tuple.
        """
        return self.__as_tuple

    # Protected

    @property
    def __as_dict(self):
        items = OrderedDict()
        for key in ['major', 'minor', 'micro', 'level', 'serial']:
            items[key] = getattr(self, key)
        return items

    @property
    def __as_str(self):
        items = [self.major, self.minor, self.micro]
        if self.level != 'final':
            items.append(self.level)
        return '.'.join(map(str, items))

    @property
    def __as_tuple(self):
        return tuple(self.__as_dict.values())
