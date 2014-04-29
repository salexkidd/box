import os

#TODO: add onerror
def balanced_walk(*dirpathes, sorter=sorted):
    """Recursevly yield sorted filepathes from top to bottom of directory tree
    
    Function doesn't support symbolic links.
    
    :param str dirpath: directory path 
    :param function(pathes) sorter: function to sort paths
    :returns generator: filepath generator
    """
    dirpathes = list(dirpathes)
    inner_filepathes = []
    inner_dirpathes = []
    for dirpath in dirpathes:
        for name in os.listdir(dirpath):
            path = os.path.join(dirpath, name)
            if os.path.islink(path):
                continue
            elif os.path.isfile(path):
                inner_filepathes.append(path)            
            elif os.path.isdir(path):
                inner_dirpathes.append(path)         
    inner_filepathes = sorter(inner_filepathes)
    inner_dirpathes = sorter(inner_dirpathes)
    yield from inner_filepathes
    if inner_dirpathes:
        yield from balanced_walk(*inner_dirpathes)