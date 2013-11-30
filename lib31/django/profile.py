from abc import ABCMeta, abstractmethod

class Profile(metaclass=ABCMeta):
    
    #Public
    
    def export(self, scope):
        for name in dir(self):
            if not name.startswith('_'):
                scope[name.upper()] = getattr(self, name)
                
    #Abstract settings
    
    @property
    @abstractmethod
    def root_urlconf(self):
        pass #pragma: no cover

    @property
    @abstractmethod
    def secret_key(self):
        pass #pragma: no cover
    
    #Debug settings
    
    debug = False
    
    @property
    def template_debug(self):
        return self.debug
    
    #Internationalization
    #https://docs.djangoproject.com/en/1.6/topics/i18n/
    
    language_code = 'en-us'  
    time_zone = 'UTC'
    use_l18n = True
    use_l10n = True
    use_tz = True
    
    #Application definition
    
    installed_apps = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',        
    )
    
    middleware_classes = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )
    
    #Databases
    #https://docs.djangoproject.com/en/1.6/ref/settings/#databases
    
    databases = {}