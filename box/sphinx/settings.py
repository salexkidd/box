from sphinx.config import Config 
from ..functools import cachedproperty
from ..settings import Settings

class Settings(Settings):

    #Public

    def __getattr__(self, name):
        try:
            return getattr(self._defaults, name)
        except AttributeError:
            raise AttributeError(name)
        
    #Protected
    
    @cachedproperty
    def _defaults(self):
        return Config(None, None, {}, None)
        