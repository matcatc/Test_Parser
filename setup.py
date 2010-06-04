'''
@date Jun 4, 2010
@author Matthew A. Todd
'''

from distutils.core import setup

setup(name='Test Parser',
        version='0.1',
        packages=['src/BoostTestParser',
                'src/BoostTestParser.Common',
                'src/BoostTestParser.Model',
                'src/BoostTestParser.Parser',
                'src/BoostTestParser.TestResults',
                'src/BoostTestParser.View',
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

