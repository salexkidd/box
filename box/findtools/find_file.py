from .find_files import find_files

class find_file(find_files):

    #Pritected

    @property
    def _builtin_reducers(self):
        return []