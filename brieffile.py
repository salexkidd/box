from brief import FileInput, FileOutput
from briefbooks import PackageBrief

class Brief(PackageBrief):

    #Public
    
    input = FileInput('package.in')
    output = FileOutput('package.py')