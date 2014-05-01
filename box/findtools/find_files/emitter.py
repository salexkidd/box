import os
from ...itertools import MapReduceEmitter

class FindFilesEmitter(MapReduceEmitter):

    #Public

    @property
    def filename(self):
        return os.path.basename(self.filepath)