import os
import re
import importlib.machinery

class ObjectLoader:

    #Public

    def load(self, path, file_pattern, recursively=False):
        for file in self._find_files(path, file_pattern, recursively):
            for module in self._import_modules(file):
                for obj in self._get_objects(module):
                    yield obj
            
    #Protected
    
    def _find_files(self, path, file_pattern, recursively=False):
        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                if re.match(file_pattern, filename):
                    file = os.path.join(dirpath, filename)
                    yield file
            if not recursively and dirpath == path:
                break
    
    def _import_modules(self, file):
        try:
            loader = importlib.machinery.SourceFileLoader(file, file)
            module = loader.load_module(file)
            yield module
        except Exception:
            pass
        
    def _get_objects(self, module):
        for name in dir(module):
            try:
                obj = getattr(module, name)
                if self._filter_object(obj, module, name):
                    yield obj
            except Exception:
                pass
    
    def _filter_object(self, obj, module, name):
        if name.startswith('_'):
            return False
        return True