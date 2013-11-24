from django.template import RequestContext, Template

class ApplicationRequestContext(RequestContext):
    
    #Public
    
    default = {} 
    
    def __init__(self, request, data={}, inheritance=True):
        res = self.default.copy()
        res.update(data)
        res.update({'base': self._get_base(inheritance)})                
        super(ApplicationRequestContext, self).__init__(request, res)
    
    #Protected
        
    def _get_base(self, inheritance):
        if not inheritance:
            return Template('')
        else:
            return None