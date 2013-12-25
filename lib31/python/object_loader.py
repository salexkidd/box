import os
import re
import importlib.machinery

class ObjectLoader:

    #Public

    def load(self, base_dir, file_pattern):
        files = self._find_files(base_dir, file_pattern)
        modules = self._import_modules(files)
        objects = self._get_objects(modules)
        return objects
            
    #Protected
    
    def _find_files(self, base_dir, file_pattern=''):
        files = []
        for dir_path, _, file_names in os.walk(base_dir):
            for file_name in file_names:
                if re.match(file_pattern, file_name):
                    files.append(os.path.join(dir_path, file_name))
        return files
    
    def _import_modules(self, files):
        modules = []
        for file in files:
            loader = importlib.machinery.SourceFileLoader(file, file)
            module = loader.load_module(file)
            modules.append(module)
        return modules
        
    def _get_objects(self, modules):
        objects = []
        for module in modules:
            for name in dir(module):
                obj = getattr(module, name)
                if self._filter_object(obj, module, name):
                    objects.append(obj)
        return objects
    
    def _filter_object(self, obj, module, name):
        if name.startswith('_'):
            return False
        else:
            return True