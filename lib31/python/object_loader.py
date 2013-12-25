import os
import re
import inspect
import importlib.machinery

class ObjectLoader:

    #Public

    @classmethod
    def load(cls, base_dir, file_pattern):
        files = cls._find_files(base_dir, file_pattern)
        modules = cls._import_modules(files)
        objects = cls._get_objects(modules)
        return objects
            
    #Protected
    
    @staticmethod
    def _find_files(base_dir, file_pattern=''):
        files = []
        for dir_path, _, file_names in os.walk(base_dir):
            for file_name in file_names:
                if re.match(file_pattern, file_name):
                    files.append(os.path.join(dir_path, file_name))
        return files
    
    @staticmethod    
    def _import_modules(files):
        modules = []
        for file in files:
            loader = importlib.machinery.SourceFileLoader(file, file)
            module = loader.load_module(file)
            modules.append(module)
        return modules
        
    @staticmethod        
    def _get_objects(modules):
        objects = []
        for module in modules:
            for name in dir(module):
                attr = getattr(module, name)
                if inspect.getmodule(attr) == module:
                    objects.append(attr)
        return objects