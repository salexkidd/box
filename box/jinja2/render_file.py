import os
from .object_context import ObjectContext
from .object_template import ObjectTemplateMixin

class RenderFile:
    
    #Public
    
    def __call__(self, context, source, target=None):
        template = self._get_template(source)
        context = self._get_context(context)
        text = template.render(context)
        if target:
            with self._open_function(target, 'w') as file:
                file.write(text)
        else:
            return text
            
    #Protected
    
    _object_context_class = ObjectContext
    _open_function = staticmethod(open)
    
    def _get_template(self, source):
        dirname, filename = os.path.split(os.path.abspath(source))
        loader = self._file_system_loader_class(dirname)
        environment = self._environment_class(loader=loader)
        environment.template_class = self._module_template_class
        template = environment.get_template(filename)
        return template
    
    def _get_context(self, context):
        context = self._module_context_class(self.meta_module)
        return context
    
    def _get_environment_class(self):
        from jinja2 import Environment
        return Environment
    
    def _get_file_system_loader_class(self):
        from jinja2 import FileSystemLoader
        return FileSystemLoader    
    
    def _get_object_template_class(self):
        from jinja2 import Template
        class ObjectTemplate(ObjectTemplateMixin, Template): pass
        return ObjectTemplate
    
    
render_file = RenderFile()