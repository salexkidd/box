import os

def balanced_walk(*basedirs, sorter=sorted, onerror=None):
    """Recursevly yield sorted filepathes from top to bottom of directory tree.

    :param str basedir: base directory path 
    :param function(pathes) sorter: function to sort paths
    :param function(os.error) onerror: function to handle os.errors
    
    :returns generator: filepath generator
    
    Function doesn't support symbolic links.    
    """
    basedirs = list(basedirs)
    filepathes = []
    dirpathes = []
    for basedir in basedirs:
        try:
            for name in os.listdir(basedir):
                path = os.path.join(basedir, name)
                if os.path.islink(path):
                    continue
                elif os.path.isfile(path):
                    filepathes.append(path)            
                elif os.path.isdir(path):
                    dirpathes.append(path)      
        except os.error as exception:
            if onerror is not None:
                onerror(exception)
            return   
    filepathes = sorter(filepathes)
    dirpathes = sorter(dirpathes)
    yield from filepathes
    if dirpathes:
        yield from balanced_walk(*dirpathes)