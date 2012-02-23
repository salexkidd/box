import sys
import subprocess
from abc import ABCMeta, abstractproperty

class ProgramRunclass(object):
    
    __metaclass__ = ABCMeta

    @abstractproperty
    def package(self):
        pass #pragma: no coverage
    
    def version(self):
        """
        Print current package version.
        """
        print(self.package.version)
        
    def release(self, step, level='final'):
        """
        Release package with version step and level.
        Steps:
        - major
        - minor
        - micro
        - level
        """
        version = self.package.version.next(step=step, level=level)
        if version == self.package.version:
            sys.exit('Incorrect step/level')  
        if self.test() != 0:
            sys.exit('Tests failed')    
        if not self._confirm('Release version {version}?'.
                        format(version=version)):
            sys.exit('Aborted by user')
        self.commit()
        self.package.version = version 
        self.commit(message='updated version')
        self.push(branch='develop')
        self.checkout(branch='master')
        self.merge(branch='develop')
        self.tag(name=self.package.version)
        self.push(branch='master', tags=True)
        self.register()
        self.clean()
        self.checkout(branch='develop')
            
    def test(self):
        """
        Test package.
        """
        command = ['nosetests']
        return subprocess.call(command)            
    
    def register(self):
        """
        Register package.
        """
        command = ['sudo', 'python', 'setup.py', 
                   'register', 'sdist', 'upload']
        return subprocess.call(command)
    
    def clean(self):
        command = ['sudo', 'rm', '-rf', 
                   'dist', 'build', '*.egg-info']
        return subprocess.call(' '.join(command), shell=True)
           
    def commit(self, message=None):
        """
        Commit changes with message.
        """
        command = ['git', 'commit', '-a']
        if message:
            command.append('-m')
            command.append(message)
        subprocess.call(command)
        
    def tag(self, name):
        """
        Add tag name.
        """
        command = ['git', 'tag', name]
        subprocess.call(command)
        
    def checkout(self, branch):
        """
        Checkout branch.
        """
        command = ['git', 'checkout', branch]
        subprocess.call(command)
        
    def merge(self, branch):
        """
        Merge branch.
        """
        command = ['git', 'merge', branch]
        subprocess.call(command)
        
    def push(self, branch, tags=False):
        """
        Push branch to origin.
        """
        command = ['git', 'push', 'origin', branch]
        if tags:
            command.append('--tags')
        subprocess.call(command)
        
    def _confirm(self, text):
        response = raw_input('{text} [y/n]: '.format(text=text))
        if response.lower() == 'y':
            return True
        else:
            return False