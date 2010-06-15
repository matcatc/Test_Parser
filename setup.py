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
from distutils.command.sdist import sdist as _sdist
import subprocess, os.path


def pre_sdist():
    print("building documentation")
    subprocess.check_call("./build_documentation.sh")
    
def post_sdist():
    pass


class my_sdist(_sdist):
    '''
    customizing sdist so that we can have it compile the documentation
    '''
    def run(self):
        pre_sdist()
        _sdist.run(self)
        post_sdist()



def find_data_files(directory):
    '''
    Searches through a given directory using os.walk() and includes
    ALL files found.
    
    Based of code I found here: http://github.com/django/django/blob/master/setup.py
    Which is part of the django project, licensed under BSD license.
    I simply cut out stuff I found useless and restructured files.append(...)
    
    @date June 10, 2010
    @author Matthew A. Todd
    '''
    files = []
    for dirpath, dirnames, filenames in os.walk(directory):
        # Ignore dirnames that start with '.'
        for i, dirname in enumerate(dirnames):
            if dirname.startswith('.'): del dirnames[i]
        if filenames:
            for f in filenames:
                if not f.startswith('.'):           # ignore hidden files (.abc)
                    files.append(os.path.join(dirpath, f))
    return files

data_files = find_data_files('doc/doxygen/html')
data_files += find_data_files('doc/docbook')
#print("DEBUG: data_files:" + "\n".join(data_files) + "\n\n")


setup(name='Test Parser',
        version='0.1',
        description='Test Parser displays the results from a given test run',
        author='Matthew A. Todd',
        author_email='matcatprg@yahoo.com',
        url='http://github.com/matcatc/Test_Parser',
        
        cmdclass={'sdist': my_sdist},
        
        package_dir = {"": "src"},
        packages=['TestParser',
                'TestParser.Common',
                'TestParser.Model',
                'TestParser.Parser',
                'TestParser.TestResults',
                'TestParser.View',
                'TestParser_tests',
                'TestParser_tests.Common',
                'TestParser_tests.Model',
                'TestParser_tests.Parser',
                'TestParser_tests.TestResults',
                'TestParser_tests.View',
                ],
        scripts=['src/main.py', 'src/test_runner.py'],
        
        package_data = {'TestParser.View' : ['*.ui'],
                        'TestParser_tests.Model': ['Boost_Test'],
                        'TestParser_tests.Parser': ['xml']},
        
        # TODO: data files (docs)
        data_files = data_files
        )

