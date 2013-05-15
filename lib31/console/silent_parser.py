from argparse import ArgumentParser
    
class SilentParser(ArgumentParser):
    
    #Public
    
    def error(self, message):
        raise SilentParserException(message)
    
    
class SilentParserException(Exception):
    
    #Public
    
    pass