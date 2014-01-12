#Builded for {{ name }} {{ version }} from _templates/setup.tpl

import os
from setuptools import find_packages, setup

package = {

	#Main

    'name': '{{ pypi_name }}',
	'version':'{{ version }}',
	'packages': find_packages(
        os.path.dirname(__file__) or '.', 
        exclude=['tests*']
    ),
	'include_package_data': True,
    'tests_require': ['nose'],
    'test_suite': 'nose.collector',
    
    #Description
    
    'author': '{{ author }}',
    'author_email': '{{ author_email }}',
    'classifiers': {{ classifiers }},       
    'description': '{{ description }}',
    'download_url':'https://github.com/{{ github_user }}/{{ name }}/tarball/{{ version }}',
    'license': '{{ license }}',
    'maintainer': '{{ maintainer }}',
    'maintainer_email': '{{ maintainer_email }}',
    'platforms': ['Unix'],
    'url': 'https://github.com/{{ github_user }}/{{ name }}',
    'long_description': '''{{ long_description }}''',        
    
}

if __name__ == '__main__':
    setup(**package)