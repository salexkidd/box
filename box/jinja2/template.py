import sys
from .context import ObjectContext

class TemplateMixin:
    
    #Public
    
    def render(self, context):
        if self._is_regular_context(context):
            return super().render(context)
        else:
            try:
                context = ObjectContext(context) 
                context = self.new_context(context, shared=True)
                return self._concat_function(self.root_render_func(context))
            except Exception:
                exc_info = sys.exc_info()
                return self.environment.handle_exception(exc_info, True)
    
    #Protected
    
    def _is_regular_context(self, context):
        if (hasattr(context, '__contains__') and 
            hasattr(context, '__getitem__')):
            return True
        else:
            return False
        
    @property
    def _concat_function(self):
        from jinja2.utils import concat
        return concat