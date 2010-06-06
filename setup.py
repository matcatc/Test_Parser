#!/usr/bin/python3
'''
@date Jun 4, 2010
@author Matthew A. Todd
'''

from distutils.core import setup

setup(name='Test Parser',
        version='0.1',
        packages=['src/TestParser',
                'src/TestParser.Common',
                'src/TestParser.Model',
                'src/TestParser.Parser',
                'src/TestParser.TestResults',
                'src/TestParser.View',
                'src/tests',
                'src/tests.Common',
                'src/tests.Model',
                'src/tests.Parser',
                'src/tests.TestResults',
                'src/tests.View',
                ],
        py_modules=['src/main', 'src/test_runner'],    
        scripts=['src/main.py', 'src/test_runner.py']
        )

