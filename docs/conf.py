import box
from box.sphinx import Settings

class Settings(Settings):
    
    #Build
        
    extensions = ['sphinx.ext.autodoc']
    master_doc = 'index'
    exclude_patterns = ['_build']
    pygments_style = 'sphinx'

    #Project
    
    project = 'box'
    author = 'roll'
    copyright = '2014, Respect31'
    version = box.version
    
    
locals().update(Settings())