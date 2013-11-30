from abc import ABCMeta, abstractmethod
from django.conf import global_settings

class Profile(metaclass=ABCMeta):
    
    #Public
    
    def __getattr__(self, name):
        try:
            return getattr(global_settings, name.upper())
        except AttributeError:
            profile_name = self.__class__.__name__
            raise AttributeError(
                'Profile "{0}" has no "{1}" attribute'.
                format(profile_name, name))
    
    def export(self, scope):
        for name in dir(self):
            if not name.startswith('_'):
                scope[name.upper()] = getattr(self, name)