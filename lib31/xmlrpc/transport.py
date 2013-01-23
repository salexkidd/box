from xmlrpclib import Transport, ProtocolError

class CookieSessionTransport(Transport):
    
    #Public
    
    def __init__(self, cookie_session_key):
        Transport.__init__(self)
        self.mycookies = None
        self.mysessid = None
        self.cookie_session_key = cookie_session_key

    
    def request(self, host, handler, request_body, verbose = 0):
        h = self.make_connection(host)
        if verbose:
            h.set_debuglevel(1)
        self.send_request(h, handler, request_body)
        self.send_host(h, host)
        if self.mysessid is not None:
            h.putheader("Cookie", "%s=%s" % (self.cookie_session_key, self.mysessid))
        self.send_user_agent(h)
        
        self.send_content(h, request_body)
        
        resp = h.getresponse(buffering = True)

        if self.mysessid is None:
            self.mycookies = self._parse_cookie(resp.getheader('set-cookie') )
            if self.mycookies.has_key(self.cookie_session_key):
                self.mysessid = self.mycookies[self.cookie_session_key]
        
        if resp.status != 200:
            raise ProtocolError(
                host + handler,
                resp.status, resp.msg,
                resp.getheaders()
            )
        
        self.verbose = verbose
        
        return self.parse_response(resp)
    
    #Protected
    
    def _parse_cookie(self,s):
        if s is None: 
            return {self.cookie_session_key:None}
        ret = {}
        tmp = s.split(';')
        for t in tmp:
            coppia = t.split('=')
            k = coppia[0].strip()
            v = coppia[1].strip()
            ret[k] = v
        return ret    