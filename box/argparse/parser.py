from argparse import ArgumentParser

class Parser(ArgumentParser):
    
    #Public
    
    def __init__(self, *args, exception=None, **kwargs):
        self._exception = exception
        super().__init__(*args, **kwargs)
    
    def error(self, message):
        if self._exception:
            raise self._exception(message)
        else:
            super().error(message)
            