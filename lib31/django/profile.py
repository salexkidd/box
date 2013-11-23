from abc import ABCMeta, abstractproperty

class Profile(metaclass=ABCMeta):
    
    #Public
    
    #Root urlconf
    @abstractproperty
    def root_urlconf(self):
        pass #pragma: no cover

    #Make this unique, and don't share it with anybody.
    @abstractproperty
    def secret_key(self):
        pass #pragma: no cover
    
    #Site identifier
    site_id = 1 
    
    #Debug
    debug = False
    
    #Template debug
    @property
    def template_debug(self):
        return self.debug

    #('Your Name', 'your_email@example.com'),
    admins = ()
    
    #Managers
    @property
    def managers(self):
        return self.admins
    
    #Local time zone for this installation. 
    #Choices can be found here:
    #http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
    #although not all choices may be available on 
    #all operating systems. In a Windows environment 
    #this must be set to your system time zone.
    time_zone = 'America/Chicago'
    
    #Language code for this installation. 
    #All choices can be found here:
    #http://www.i18nguy.com/unicode/language-identifiers.html
    language_code = 'en-us'    

    
    #If you set this to False, 
    #Django will make some optimizations so as not
    #to load the internationalization machinery.
    use_l18n = True
    
    #If you set this to False, 
    #Django will not format dates, numbers and
    #calendars according to the current locale.
    use_l10n = True

    # If you set this to False, 
    # Django will not use timezone-aware datetimes.
    use_tz = True
    
    #Installed applications
    installed_apps = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admin',
        'django.contrib.admindocs',
    )
    
    #Middleware classes to process request and response
    middleware_classes = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )
    
    #Databases
    databases = {}
    
    #Absolute filesystem path to the directory 
    #that will hold user-uploaded files.
    #Example: "/home/media/media.lawrence.com/media/"
    @abstractproperty    
    def media_root(self):
        pass #pragma: no cover

    #URL that handles the media served from MEDIA_ROOT. 
    #Make sure to use a trailing slash.
    #Examples: "http://media.lawrence.com/media/", 
    #"http://example.com/media/"
    media_url = '/uploads/'

    #Absolute path to the directory 
    #static files should be collected to.
    #Don't put anything in this directory yourself; 
    #store your static files in apps' 
    #"static/" subdirectories and in STATICFILES_DIRS.
    #Example: "/home/media/media.lawrence.com/static/"
    @abstractproperty    
    def static_root(self):
        pass #pragma: no cover
    
    #URL prefix for static files.
    #Example: "http://media.lawrence.com/static/"
    static_url = '/staticfiles/'
    
    #Additional locations of static files
    #Put strings here, like "/home/html/static" or 
    #"C:/www/django/static".
    #Always use forward slashes, even on Windows.
    #Don't forget to use absolute paths, not relative paths.
    staticfiles_dirs = ()
    
    #List of finder classes that know how to find static files in
    #various locations.
    staticfiles_finders = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'matrix.applications.django.library.staticfiles_finders.CustomAppDirectoriesFinder',
        #'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )
    
    #List of callables that know how to import 
    #templates from various sources.
    template_loaders = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        #'django.template.loaders.eggs.Loader',
    )
    
    #Put strings here, like "/home/html/django_templates" 
    #or "C:/www/django/templates".
    #Always use forward slashes, even on Windows.
    #Don't forget to use absolute paths, not relative paths.    
    template_dirs = ()
    
    #Template context processors
    template_context_processors = (                                   
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.contrib.messages.context_processors.messages',
    )

    #A sample logging configuration. The only tangible logging
    #performed by this configuration is to send an email to
    #the site admins on every HTTP 500 error when DEBUG=False.
    #See http://docs.djangoproject.com/en/dev/topics/logging for
    #more details on how to customize your logging configuration.
    logging = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }

    #Raw Django adapter 
    def export(self, scope):
        for name in dir(self):
            if not name.startswith('_'):
                scope[name.upper()] = getattr(self, name)