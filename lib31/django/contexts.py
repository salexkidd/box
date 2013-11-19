from django.template import RequestContext, Template

class ApplicationRequestContext(RequestContext):
    
    #Public
    
    default = {} 
    
    def __init__(self, request, data={}, inheritance=True):
        res = self.default.copy()
        res.update(data)
        res.update({'base': self.__get_base(inheritance)})                
        super(ApplicationRequestContext, self).__init__(request, res)
    
    #Private
        
    def __get_base(self, inheritance):
        if not inheritance:
            return Template('')
        else:
            return None