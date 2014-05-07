import os

def balanced_walk(dirpath=None, *, sorter=None, onerror=None):
    """Recursevly yield (dirpathes, filepathes) tuple 
    level by level from top to bottom of directory tree.

    :param str/list dirpath: top directory path or list of pathes
    :param function(pathes) sorter: function to sort pathes
    :param function(os.error) onerror: function to handle os.errors
    
    :returns generator: (dirpathes, filepathes) generator
    
    Function doesn't support symbolic links. 
    """
    if not isinstance(dirpath, list):
        dirpathes = [dirpath]
    else:
        dirpathes = dirpath
    inner_filepathes = []
    inner_dirpathes = []
    for dirpath in dirpathes:
        try:
            if dirpath == None:
                names = os.listdir()
            else:
                names = os.listdir(dirpath)
            for name in names:
                if dirpath == None:
                    path = name
                else:
                    path = os.path.join(dirpath, name)
                if os.path.islink(path):
                    continue
                elif os.path.isfile(path):
                    inner_filepathes.append(path)            
                elif os.path.isdir(path):
                    inner_dirpathes.append(path)
        except os.error as exception:
            if onerror is not None:
                onerror(exception)
            return
    if sorter != None:
        inner_filepathes = sorter(inner_filepathes)
        inner_dirpathes = sorter(inner_dirpathes)
    yield (inner_dirpathes, inner_filepathes)
    if inner_dirpathes:
        yield from balanced_walk(
            inner_dirpathes, 
            sorter=sorter, 
            onerror=onerror)