from ..functools import cachedproperty
from ..settings import Settings

class Settings(Settings):
    """Class representation of sphinx conf.py.
    
    Just put code like this in conf.py module and use inheritance from 
    default sphinx settings and other class benefits. It gives a opportunity 
    to not operate with big config file filled by standard settings and 
    see only important things::
    
      from box.sphinx import Settings

      class Settings(Settings):
        
          #Documentation:
          #http://sphinx-doc.org/config.html
          
          #Project
    
          project = 'box'
        
      locals().update(Settings())
    """

    #Public

    def __getattr__(self, name):
        try:
            return getattr(self._defaults, name)
        except AttributeError:
            raise AttributeError(name)
    
    @property    
    def release(self):
        return self.version
    
    @property     
    def latex_documents(self):
        return [(
            self.master_doc, 
            self.project+'.tex', 
            self.project+' Documentation', 
            self.author, 
            'manual')]
     
    @property          
    def man_pages(self):
        return [(
            self.master_doc, 
            self.project, 
            self.project+' Documentation', 
            [self.author], 
            1)]
        
    @property          
    def texinfo_documents(self): 
        return [(
            self.master_doc,  
            self.project, 
            self.project+' Documentation',
            self.author,
            self.project, 
            'One line description of project.',
            'Miscellaneous')]        
        
    #Protected
    
    @cachedproperty
    def _defaults(self):
        from sphinx.config import Config 
        return Config(None, None, {}, None)       