from argparse import ArgumentParser
from .exception import CommandException
    
class CommandArgumentParser(ArgumentParser):
    
    #Public
    
    def error(self, message):
        raise CommandException(message)