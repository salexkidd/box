import os

#TODO: add onerror
def balanced_walk(*dirpathes):
    """Recursevly yield sorted filepathes from top to bottom of directory tree
    
    Function doesn't support symbolic links.
    
    :param dirpath: directory path 
    :returns generator: filepath generator
    """
    dirpathes = list(dirpathes)
    dirpathes.sort()
    for dirpath in dirpathes:
        inner_filepathes = []        
        inner_dirpathes = []
        for name in os.listdir(dirpath):
            path = os.path.join(dirpath, name)
            if os.path.islink(path):
                continue
            elif os.path.isfile(path):
                inner_filepathes.append(path)            
            elif os.path.isdir(path):
                inner_dirpathes.append(path)         
        inner_filepathes.sort()
        yield from inner_filepathes
        yield from balanced_walk(*inner_dirpathes)