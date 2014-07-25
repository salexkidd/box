from collections import OrderedDict

class Version(str):
    """Version representation.

    :param dict kwargs: key=value pairs to override version elements

    Usage example::

      >>> from box.packtools import Version
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

    .. seealso:: Python versioning: `sys.version_info <https://docs.python.org/3/library/sys.html#sys.version_info>`_
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
        if version != None:
            ekwargs = version._as_dict
            ekwargs.update(kwargs)
        # Buffer version
        version = str.__new__(cls)
        vars(version).update(ekwargs)
        # Actual version
        version = str.__new__(cls, version._as_str)
        vars(version).update(ekwargs)
        return version

    @property
    def info(self):
        """Version as a tuple.
        """
        return self._as_tuple

    # Protected

    @property
    def _as_dict(self):
        result = OrderedDict()
        for key in ['major', 'minor', 'micro', 'level', 'serial']:
            result[key] = getattr(self, key)
        return result

    @property
    def _as_str(self):
        items = [self.major, self.minor, self.micro]
        if self.level != 'final':
            items.append(self.level)
        return '.'.join(map(str, items))

    @property
    def _as_tuple(self):
        return tuple(self._as_dict.values())
