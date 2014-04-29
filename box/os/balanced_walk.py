import os

#TODO: add onerror
def balanced_walk(dirpathes):
    """Recursevly yield filepathes from top to bottom of directory tree
    
    Function doesn't support symbolic links.
    
    :param list dirpathes: paths of top directories 
    :returns generator: filepath generator
    """
    for dirpath in dirpathes:
        inner_filepathes = []        
        inner_dirpathes = []
        for path in os.listdir(dirpath):
            if os.path.islink(path):
                continue
            elif os.path.isfile(path):
                inner_filepathes.append(path)            
            elif os.path.isdir(path):
                inner_dirpathes.append(path)         
        inner_filepathes.sort()
        inner_dirpathes.sort()
        yield from inner_filepathes
        yield from balanced_walk(inner_dirpathes)