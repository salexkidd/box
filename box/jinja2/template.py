import sys
from .context import ObjectContext

class TemplateMixin:
    """Mixin adds to jinja2.Template support of :class:`ObjectContext`.
    """
    
    #Public
    
    def render(self, context):
        if self._is_regular_context(context):
            return super().render(context)
        else:
            try:
                context = ObjectContext(context) 
                context = self.new_context(context, shared=True)
                return self._concat(self.root_render_func(context))
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
    def _concat(self):
        from jinja2.utils import concat
        return concat