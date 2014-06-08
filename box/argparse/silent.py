from argparse import ArgumentParser

class SilentArgumentParser(ArgumentParser):
    """Argument parser with raising exception instead of program exit.
    """
    
    #Public
    
    def error(self, message):
        raise SilentArgumentParserException(message)
    
    
class SilentArgumentParserException(Exception): 
    """Exception to be rased if parse is failed
    """
    
    #Public
    
    pass