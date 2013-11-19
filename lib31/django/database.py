import subprocess

class Database:
    
    #Public
    
    def __init__(self, name, user):
        self._name = name
        self._user = user

    def create(self):
        subprocess.call((
            'mysql -u{user} -e '
            '"CREATE DATABASE IF NOT EXISTS {name} '
            ' CHARACTER SET utf8 COLLATE utf8_general_ci"'
            ).format(
                user=self._user,
                name=self._name
            ),
            shell=True,
        )
    
    def delete(self):
        subprocess.call((
            'mysql -u{user} -e '
            '"DROP DATABASE IF EXISTS {name}"'
            ).format(
                user=self._user,
                name=self._name
            ),
            shell=True,
        )
    
    def clean(self):
        self.delete()
        self.create()
      
    def save(self, path, tables=[]):
        subprocess.call((
            'mysqldump -u{user} '
            '--opt --complete-insert --skip-comments '
            '--skip-add-drop-table '
            '{name} {tables} > {path}'
            ).format(
                user=self._user,
                name=self._name,
                tables=' '.join(tables),    
                path=path,
            ),
            shell=True,
        ) 
             
    def load(self, path):
        subprocess.call((
            'mysql -uroot '
            '{name} < {path} '
            '--force'
            ).format(
                user=self._user,
                name=self._name,                             
                path=path,
            ),
            shell=True,
        )