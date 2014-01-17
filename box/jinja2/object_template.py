import sys

class ObjectTemplateMixin:
    
    #Public
    
    def render(self, object_context):
        try:
            context = self.new_context(object_context, shared=True)
            return self._concat_function(self.root_render_func(context))
        except Exception:
            exc_info = sys.exc_info()
            return self.environment.handle_exception(exc_info, True)
    
    #Protected
    
    @property
    def _concat_function(self):
        from jinja2.utils import concat
        return concat