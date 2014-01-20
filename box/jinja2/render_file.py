import os
from .object_context import ObjectContext
from .object_template import ObjectTemplateMixin

class RenderFile:
    
    #Public
    
    def __call__(self, *args, **kwargs):
        call = self._call_class(*args, **kwargs)
        result = call.execute()
        return result
    
    #Protected
    
    _call_class = property(lambda self: RenderFileCall)
        

class RenderFileCall:
    
    #Public
    
    def __init__(self, path, context={}, target=None):
        self._path = path
        self._context = context
        self._target = target
    
    def execute(self):
        content = self._render()
        self._write(content)
        return content
            
    #Protected
    
    _object_context_class = ObjectContext
    _open_function = staticmethod(open)
    
    def _render(self):
        return self._template.render(self._prepared_context)
    
    def _write(self, content):
        if self._target:
            with self._open_function(self._target, 'w') as file:
                file.write(content)
                
    @property
    def _template(self):
        dirpath, filename = os.path.split(self._path)
        loader = self._file_system_loader_class(dirpath)
        environment = self._environment_class(loader=loader)
        if not self._is_object_jinja2_context(self._context):        
            environment.template_class = self._object_template_class
        template = environment.get_template(filename)    
        return template
    
    @property    
    def _prepared_context(self):
        prepared_context = self._context
        if not self._is_object_jinja2_context(prepared_context):
            prepared_context = self._object_context_class(prepared_context)
        return prepared_context
    
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