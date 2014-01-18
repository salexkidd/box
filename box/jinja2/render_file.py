import os
from .object_context import ObjectContext
from .object_template import ObjectTemplateMixin

class RenderFile:
    
    #Public
    
    def __call__(self, path, context={}, target=None):
        dirpath = self._get_dirname(path)
        filename = self._get_filename(path)
        loader = self._get_loader(dirpath)
        environment = self._get_environment(loader, context)
        template = self._get_template(environment, filename)
        context = self._get_context(context)
        text = template.render(context)
        if target:
            self._write_text(text, target)
        return text
            
    #Protected
    
    _object_context_class = ObjectContext
    _open_function = staticmethod(open)
    
    def _get_dirname(self, path):
        return os.path.dirname(path)
    
    def _get_filename(self, path):
        return os.path.basename(path)
    
    def _get_loader(self, dirpath):
        return self._file_system_loader_class(dirpath)
    
    def _get_environment(self, loader, context):
        environment = self._environment_class(loader=loader)
        if not self._is_object_jinja2_context(context):        
            environment.template_class = self._object_template_class
        return environment
    
    def _get_template(self, environment, filename):
        return environment.get_template(filename)
    
    def _get_context(self, context):
        if not self._is_object_jinja2_context(context):
            context = self._object_context_class(context)
        return context
    
    def _write_text(self, text, target):
        with self._open_function(target, 'w') as file:
            file.write(text)        
    
    def _is_object_jinja2_context(self, obj):
        if hasattr(obj, '__contains__') and hasattr(obj, '__getitem__'):
            return True
        else:
            return False
    
    @property
    def _environment_class(self):
        from jinja2 import Environment
        return Environment
    
    @property
    def _file_system_loader_class(self):
        from jinja2 import FileSystemLoader
        return FileSystemLoader    
    
    @property
    def _object_template_class(self):
        from jinja2 import Template
        class ObjectTemplate(ObjectTemplateMixin, Template): pass
        return ObjectTemplate
    
    
render_file = RenderFile()