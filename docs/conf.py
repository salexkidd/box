import os
import box
from packgram.docs import Settings

class Settings(Settings):
    
    #Documentation:
    #http://sphinx-doc.org/config.html

    #Project
    
    project = 'box'
    author = 'roll'
    copyright = '2014, Respect31'
    version = box.version
    
    
locals().update(Settings())