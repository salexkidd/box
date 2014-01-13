from sphinx.config import Config 
from ..functools import cachedproperty
from ..settings import Settings

class Settings(Settings):

    #Public

    def __getattr__(self, name):
        return getattr(self._default, name)
        
    #Protected
    
    @cachedproperty
    def _default(self):
        return Config(None, None, {}, None)
        