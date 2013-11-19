from django.contrib.staticfiles.storage import AppStaticStorage
from django.contrib.staticfiles.finders import AppDirectoriesFinder

class CustomAppStaticStorage(AppStaticStorage):
    
    source_dir = 'staticfiles'


class CustomAppDirectoriesFinder(AppDirectoriesFinder):
    
    storage_class = CustomAppStaticStorage