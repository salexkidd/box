from xmlrpclib import ServerProxy
from .transport import CookieSessionTransport

class CookieSessionServerProxy(ServerProxy):
    
    #Public
    
    def __init__(self, uri, cookie_session_key, *args, **kwargs):
        kwargs['transport'] = CookieSessionTransport(cookie_session_key)
        ServerProxy.__init__(self, uri, *args, **kwargs)