import os
      
class Reader(object):
    """
    Reads files by path relatively root path.
    """
    
    def __init__(self, *args):
        """
        Instantiates class object by root path.
        Root path is positional arguments join by os.path.join. 
        """
        self.root = os.path.join(*args)
        
    def read(self, *args):
        """
        Reads file content from file path.
        File path is root and positional arguments join by os.path.join.
        """
        with open(self.path(*args)) as f:
            return f.read()
        
    def path(self, *args):
        """
        Returns root and positional arguments join by os.path.join.
        """        
        return os.path.join(self.root, *args)