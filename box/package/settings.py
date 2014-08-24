import os
import inspect
from ..find import find_objects
from .include import include


class SettingsMetaclass(type):
    """Metaclass adds extensions functionality to Settings.
    """

    # Public

    def __call__(self, settings=None, **kwargs):
        settings = dict.__new__(self)
        esettings = self._merge_extensions()
        esettings.update(settings)
        settings.__init__(settings=esettings, **kwargs)
        return settings


class Settings(dict, metaclass=SettingsMetaclass):
    """Settings representation.

    Parameters
    ----------
    settings: dict
        Dict to override settings values.
    kwargs: dict
        Key=value pairs to override settings values.

    Examples
    --------
    Following example will show common workflow and extensions::

      >>> from box.package import Settings
      >>> class Settings(Settings):
      ...   attr1 = 'value1'
      ...   attr2 = 'value2'
      ...   _extensions = [{'attr2': 'new2'}, 'path_to_user_settings']
      ...
      >>> s = Settings(attr1='new1')
      >>> s
      {'attr1': 'new1', 'attr2': 'new2'}

    In the example above program also checks path_to_user_settings:

    - if file exists and contain Settings subclass program will use it
    - if file doesn't exist program will create stub Settings file
    """

    # Public

    def __init__(self, settings=None, **kwargs):
        if settings:
            vars(self).update(settings)
        vars(self).update(kwargs)
        self.update(self._as_dict)

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        self.update(self._as_dict)

    def __delattr__(self, name):
        super().__delattr__(name)
        self.clear()
        self.update(self._as_dict)

    # Protected

    _extensions = []
    """List of extensions.

    Members should be following types:

    - if element is a dict it just override settings values
    - if element is a string it should be a filepath to another Settings
    """

    @property
    def _as_dict(self):
        items = {}
        for name in dir(self):
            if not name.startswith('_'):
                attr = getattr(self, name)
                if callable(attr):
                    if not getattr(attr, include.attribute_name, False):
                        # Callable doesn't use @include decorator - skip
                        continue
                items[name] = attr
        return items

    @classmethod
    def _merge_extensions(cls):
        settings = {}
        for extension in cls._extensions:
            try:
                if isinstance(extension, str):
                    if os.path.isfile(extension):
                        # Extension's settings file already exists
                        Extension = cls._find_extension_class(extension)
                        extension = Extension()
                    else:
                        # Extension's settings file has to be created
                        cls._create_extension_class(extension)
                        extension = {}
                settings.update(extension)
            except Exception as error:
                cls._handle_extension_error(extension, error)
                continue
        return settings

    @classmethod
    def _find_extension_class(cls, extension):
        objects = find_objects(
            filepathes=[extension],
            filters=[{'objtype': cls.__class__}],
            mappers=[lambda emitter: emitter.skip(
                inspect.getmodule(emitter.objself) != emitter.module)],
            getfirst=True)
        return objects

    @classmethod
    def _create_extension_class(cls, extension):
        dirname = os.path.dirname(extension)
        if dirname:
            os.makedirs(dirname, exist_ok=True)
        with open(extension, 'w') as file:
            file.write(
            'from box.package import Settings\n\n'
            'class Settings(Settings):\n\n'
            '    # Public\n\n'
            '    pass\n')

    @classmethod
    def _handle_extension_error(cls, extensoin, error):
        pass  # pragma: no cover
