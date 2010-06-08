#!/usr/bin/python3
'''
@date Jun 4, 2010
@author Matthew A. Todd

by Matthew A. Todd

Test Parser is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Test Parser is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Test Parser.  If not, see <http://www.gnu.org/licenses/>.
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
        
        package_data = {'TestParser.View' : ['*.ui'],
                        'tests.Model': ['Boost_Test'],
                        'tests.Parser': ['xml']}
        # TODO: data files (docs)
        )

