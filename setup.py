#!/usr/bin/python3
'''
@date Jun 4, 2010
@author Matthew A. Todd
'''

from distutils.core import setup
#from setuptools import setup, find_packages

setup(name='Test Parser',
        version='0.1',
        description='Test Parser displays the results from a given test run',
        author='Matthew A. Todd',
        author_email='matcatprg@yahoo.com',
        url='http://github.com/matcatc/Test_Parser',
        
        package_dir = {"": "src"},
        packages=['TestParser',
                'TestParser.Common',
                'TestParser.Model',
                'TestParser.Parser',
                'TestParser.TestResults',
                'TestParser.View',
                'tests',
                'tests.Common',
                'tests.Model',
                'tests.Parser',
                'tests.TestResults',
                'tests.View',
                ],
#        packages = find_packages(),
        scripts=['src/main.py', 'src/test_runner.py'],
        
        package_data = {'TestParser.View' : ['*.ui']}
        # TODO: data files (docs)
        )

