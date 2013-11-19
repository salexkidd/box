class DevelopmentHostMiddleware(object):
    
    #Public
    
    def process_request(self, request):
        request.META['HTTP_HOST'] = request.META['HTTP_HOST'].replace(':8000', '')
        
    def process_response(self, request, response):
        if 'Location' in response:
            response['Location'] = 'http://'+request.get_host()+':8000'+response['Location'] 
        return response
    
    
class TestingHostMiddleware(object):
    
    #Public
    
    def process_request(self, request):
        request.META['HTTP_HOST'] = request.META['HTTP_HOST'].replace('test.', '')
        
    def process_response(self, request, response):
        print(response.status_code)
        if 'Location' in response:
            response['Location'] = 'http://test.'+request.get_host()+response['Location'] 
        return response    